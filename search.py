import requests

from Restrant import Restaurant


def search_restaurants(URL, KEY_ID, freeword, hit_per_page=10):
    response = requests.get(URL, params={"keyid": KEY_ID, "freeword": freeword, "hit_per_page": hit_per_page})
    rests = response.json()["rest"]
    for rest in rests:
        yield Restaurant(name=rest["name"], url=rest["url"], access=rest["access"])
