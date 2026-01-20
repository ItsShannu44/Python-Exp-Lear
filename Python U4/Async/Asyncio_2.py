import asyncio , time , aiohttp

''' Used for asynchronous HTTP Requests '''

URL = ['https://google.com',
       'https://example.com',
       'https://www.python.org',
       'https://httpbin.org',
       ]

async def fetch(session, url):
    ''' One HTTP request per call '''
    start = time.time()
    try:
        async with session.get(url, timeout = 10) as resp:
            ''' A GET request is sent to the URL
                The coroutine waits for the response
                Control is returned to the event loop during '''
            ''' Wait '''
            await resp.read()
            ''' Read the full response body '''
            end = time.time()
            taken = round(end-start, 2)
            return url, resp.status, taken
        
    except Exception:
        end = time.time()
        taken = round(end - start, 2)
        return url, -1, taken
        ''' -1 represents a failure status'''

async def main():
    async with aiohttp.ClientSession() as session:
        ''' A single shared HTTP session is created '''
        ''' It is reused for all the HTTP requests '''
        results = await asyncio.gather(*(fetch(session, u) for u in URL))
        ''' All fetch coroutines are scheduled together '''
        ''' Execution waits until all requests are complete 
            Waiting time is shared by all requests '''
        
        for url, status, taken in results:
            print(f'URL {url} returned a status code {status} in {taken} seconds')
    
asyncio.run(main())