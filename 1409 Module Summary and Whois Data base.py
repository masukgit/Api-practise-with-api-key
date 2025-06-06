import requests
import json

API = 'B29DD7F7CF5B9CEFD69FCE481930483C'

# domain_name = input('Enter your domain name: ')
# url = f'https://api.ip2whois.com/v2?key={API}&domain={domain}'

domain_list = ['https://www.google.com', 'https://www.yahoo.com', 'https://www.bing.com', 'https://www.facebook.com']
for domain in domain_list:
    res = requests.get(domain)
    url = f'https://api.ip2whois.com/v2?key={API}&domain={domain}'
    if res.status_code == 200:
        data = json.loads(res.content)
        print(data)

