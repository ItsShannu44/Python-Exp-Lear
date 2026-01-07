import requests as req
try:
    response=req.get('https://dummyjson.com/post/67')
    response.raise_for_status()
    data=response.json()
    print(f'Retrived {len(data)} records')
except req.exceptions.HTTPError as e:
    print(f'HTTP Error: {e}')
except req.exceptions.ConnectionError as e:
    print(f'Connection Error: Check internet connection {e}')
except req.exceptions.Timeout as e:
    print(f'Timeout Error: Took long time to respond {e}')
except req.exceptions.RequestException as e:
    print(f'Error in making request {e}')
except ValueError:
    print(f'Error in passing the JSON response')