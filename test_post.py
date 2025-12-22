import requests
import json

def test_api_code():
 url = "https://api-dev.paidpexback.online/api/login"

 payload = {'mail': 'mytestrole@i.ua',
 'password': '1111111111',
 'domain': 'platform.paidpex'}
 files=[

 ]
 headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
 }

 response = requests.request("POST", url, headers=headers, data=payload, files=files)
 assert response.status_code == 200