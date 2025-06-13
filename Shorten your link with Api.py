from requests import get

API_KEY = '4dc6d21f79cbdcb8ffc727aec0795d572dc22'
my_url = input('Enter your url: ')
requested_url = f'http://cutt.ly/api/api.php?key={API_KEY}&short={my_url}'
res = get(requested_url)
if res.status_code == 200:
    data = res.json()
    short_url = data.get('url').get('shortLink')
    print(short_url)