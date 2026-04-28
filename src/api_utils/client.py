import requests


def get_json(url: str):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def post_json(url: str, data: dict):
    response = requests.post(url, json=data)
    response.raise_for_status()
    return response.json()
