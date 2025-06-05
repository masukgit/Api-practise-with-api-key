import requests

API_KEY = '3bb962a90629139b6d9c5f8d13cfe6b1'
city_name = input('Enetr any city name: ')
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'
units = '&units=metric'
request_url = url + units
res = requests.get(request_url)
if res.status_code == 200:
    content = res.json()
    main_data = content.get('main')
    current_temp = main_data.get('temp')
    feels_like = main_data.get('feels_like')
    max_temp = main_data.get('temp_max')
    min_temp = main_data.get('temp_min')
    wind_pressure = main_data.get('pressure')
    humidity = main_data.get('humidity')
    text = f'{city_name}\'s current temperature is {current_temp} but feels like {feels_like} degree celsius. Today\'s maximum temperature is {max_temp} degree celsius and minimum temperature is {min_temp} degree celsius. Today\'s wind pressure is {wind_pressure}, humidity is {humidity}.'
    print(text)
