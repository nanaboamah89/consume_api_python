
import requests


def api_get():
    response = requests.get('https://jsonplaceholder.typicode.com/todos1')
    if response.ok:
        return response
    else:
        return None

def api_count():
    response = api_get()
    if response.ok:
        return len(response.content)
    else:
        return None
