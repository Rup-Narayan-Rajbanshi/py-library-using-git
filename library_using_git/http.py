import requests


def fetch_json() -> dict:
    print("Using fetch json from submodule")
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()
