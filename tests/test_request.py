import requests
import responses

URL = "https://hacker-news.firebaseio.com/v0/item/8863.json"


@responses.activate
def test_response_ok():
    responses.add(responses.GET, url=URL)
    response = requests.get(URL)
    assert response.ok


@responses.activate
def test_response_status_code():
    responses.add(responses.GET, url=URL, status=200)
    response = requests.get(URL)
    assert response.status_code == 200
