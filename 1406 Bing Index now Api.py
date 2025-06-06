from requests import post
import json

API_KEY = '5e1eac989ed4449b9a1d5108c435a3c8'
my_web_url = input('Enter your url to index: ')
url = f'https://www.bing.com/indexnow?url={my_web_url}&key={API_KEY}'
res = post(url)

print(res.json())

# incomplete because needed hostting API KEY to cpanel.