import requests


BASE_URL = "https://hacker-news.firebaseio.com/v0/item/"


def get_comment_from_api(id):
    url = BASE_URL + str(id) + ".json"
    response = requests.get(url)
    return response.text
