import requests

def api_get(url):
    return requests.get(url)

def api_count(url_body):
    return len(url_body)

def api_get_record(url_body):
    return url_body.json
    