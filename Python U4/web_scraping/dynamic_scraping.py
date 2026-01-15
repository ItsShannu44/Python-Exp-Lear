import time, csv, shutil, zipfile
from pathlib import Path
from selenium import webdriver as WD
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC


#2.define the end points

URL="https://airquality.cpcb.gov.in/AQI_India/"
PROFILE_DIR=str(Path.cwd()/"chrome_profile_aqi")
#persistant chrome profile directory cookies and captcha is used accross different executions
DOWNLOAD_DIR=Path.cwd()/"AQI_Downloads"
DOWNLOAD_DIR.mkdir(parents=True,exist_ok=True)


#3 create a chrome option object
def start_driver():
    options=Options()
    options.add_argument('--window-size=1500,900')
    options.add_argument(f"--user-data-dir={PROFILE_DIR}")
    options.add_argument('--disable-gpu')
    options.add_argument('--log-level=3')
    prefs={'download.default_directory':str(DOWNLOAD_DIR.resolve()),'download.prompt_for_download':False,'download.directory_upgrade':True,'safebrowsing.enabled':True}

    #Add the dwld preferences
    options.add_experimental_option('prefs',prefs)
    return WD.Chrome(options=options)

def wait_download_complete(timeout_sec=180):
    t0=time.time()
    #Start the clock
    while time.time()-t0<timeout_sec:
        #Runs until the timeout is reached
        cr=list(DOWNLOAD_DIR.glob('*.crdownload'))
        # Checks for temp download files
        if cr:
            time.sleep(0.5)
            continue
        files=[p for p in DOWNLOAD_DIR.iterdir() if p.is_file()]
        if files:
            latest= max(files, key=lambda p:p.stat().st_mtime)
            return latest
        time.sleep(0.5)
    raise TimeoutError ('Download did not complete within the time limit')

#Define a method to check for the events
def close_blocking_modal(driver):
    time.sleep(1)
    close_xpaths=[
        "//div[@id='myModal']//button[contains(@class,'close')]",        
        "//div[@id='myModal']//button[contains(.,'Close')]",        
        "//div[@id='myModal']//button[contains(.,'OK')]",        
        "//div[@id='myModal']//button[contains(.,'I Agree')]",        
        "//div[@id='myModal']//button[contains(.,'Close')]",      
    ]
    for xp in close_xpaths:
        try:
            btn=WDW(driver,3).until(EC.element_to_be_clickable((By.XPATH, xp)))
            driver.execute_script('arguments[0].click();',btn)
            time.sleep(1)
            return
        except Exception:
            pass
    driver.execute_script('''const m=document.querySelector('#myModal');
                          if (m) m.remove();
                          const n=document.querySelector('.modal-backdrop');
                          if (n) n.remove();
                          document.body.classList.remove('modal-open');''')
    
    time.sleep(1)

    #Start the browser session

driver=start_driver()
#opens a new chrome browser window

try:
    driver.get(URL)
    WDW(driver, 300).until(lambda d: d.execute_script('return document.readyState')=='complete') #page load completion is waited for 300 sec
    rep_l=WDW(driver, 300).until(EC.element_to_be_clickable((By.XPATH,'//a[contains(.,"AQI Data Repository") or contains(.,"Repository")]'))) #repo link is located
    close_blocking_modal(driver)
    driver.execute_script('arguments[0].scrollIntoView({block:"center"})')
    time.sleep(0.5)
    driver.execute_script("arguments[0].click();",rep_l)
    WDW(driver,10).until(lambda d: len(d.window_handles) > 1) #browser tab count is verified
    if len(driver.window_handles)>1:
        driver.switch_to.window(driver.window_handles[-1])
        #Open the last tab
    WDW(driver, 180).until(EC.presence_of_all_elements_located((By.TAG_NAME,'table'))) #check for presence of table
    table=driver.find_element(By.TAG_NAME,'table')
    rows=table.find_elements(By.CSS_SELECTOR,'tr')
    #select the table element and all rows of that table element.
    downloads_log=[]
    for r in rows[1:]:
        tds=r.find_elements(By.CSS_SELECTOR,'td')
        if len(tds)<2:
            continue
        year=tds[0].text.strip()
        #extract year
        if not year.isdigit():
            continue #if no year exist then continue to the nxt row
        before=set(DOWNLOAD_DIR.iterdir())
        download_cell=tds[1]
        clickable=None
        can=download_cell.find_elements(By.CSS_SELECTOR,'a,button')
        if can:
            clickable=can[0]
        else:
            icons=download_cell.find_elements(By.CSS_SELECTOR,'i,span,div')
            if icons:
                clickable=icons[0]
        if not clickable:
            continue
        driver.execute_script('arguments[0].scrollIntoView({block:"center"});',clickable)
        time.sleep(0.2)
        driver.execute_script('arguments[0].click();',clickable)
        downloaded=wait_download_complete(timeout_sec=180)
        after=set(DOWNLOAD_DIR.iterdir())

        new=[p for p in after-before if p.is_file()]
        if new:
            downloaded=max(new, key=lambda p: p.stat().st_mtime)
    ext=downloaded.suffix.lower()
    target=DOWNLOAD_DIR/f'AQI_{year}.{ext}' #rename the file with year
    if target.exists():
        target.unlink()
    downloaded.rename(target)
    downloads_log.append([year,str(target)]) #Download rec is stored

    with open(DOWNLOAD_DIR/'downloads_index.csv','w')as f:
        w=csv.writer(f)
        w.writerow(['year','file_path'])
        w.writerows(downloads_log)
    print(f'Downloaded {len(downloads_log)} files')
    print(f'Folder : {str(DOWNLOAD_DIR)}')
  
except Exception as e:
    screenshot_path = DOWNLOAD_DIR / 'debug.png'
    driver.save_screenshot(str(screenshot_path))
    print("ERROR:", e)
    input("Press ENTER to close browser...")
    raise

finally:
    driver.quit()
