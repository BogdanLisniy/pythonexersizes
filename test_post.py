import requests
import json

def test_api_code():
 url = "https://api-dev.paidpexback.online/api/login"

 payload = {'mail': 'mytestrole@i.ua',
 'password': '1111111111',
 'domain': 'platform.paidpex'}

 response = requests.request("POST", url, json=payload)
 assert response.status_code == 200