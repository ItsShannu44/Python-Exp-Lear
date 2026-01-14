import time, csv, shutil, zipfile
from pathlib import path
from selenium import webdriver as WD
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC


#2.define the end points

URL="https://airquality.cpcb.gov.in/AQI_India/"
PROFILE_DIR=str(path.cwd()/"chrome_profile_aqi")
#persistant chrome profile directory cookies and captcha is used accross different executions
DOWNLOAD_DIR=path.cwd()/"AQI_Downloads"
DOWNLOAD_DIR.mkdir(parents=True,exit_ok=True)


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