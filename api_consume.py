import requests

def api_get(url):
    return requests.get(url)

def api_count(url_body):
    return len(url_body)
    