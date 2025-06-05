import requests
import json

food_name = []
first_letter = input('Enter any letter to search: ')
url = f'https://www.themealdb.com/api/json/v1/1/search.php?f={first_letter}'
res = requests.get(url)
if res.status_code == 200:
    content = json.loads(res.text)
    meals = content.get('meals')
    for meal in meals:
        meal_name = meal.get('strMeal')
        food_name.append(meal_name)
print(food_name)



categories_name = []
url = 'https://www.themealdb.com/api/json/v1/1/categories.php'
res = requests.get(url)
if res.status_code == 200:
    content = json.loads(res.content)
    food_categories = content.get('categories')
    for item in food_categories:
        category_name = item.get('strCategory')
        categories_name.append(category_name)
print(categories_name)

