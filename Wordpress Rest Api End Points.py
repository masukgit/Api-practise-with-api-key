import requests

post = 'https://nijhoom.com/wp-json/wp/v2/posts'
post_ids = []
res = requests.get(post)
if res.status_code == 200:
    data =res.json()
    for post in data:
        post_ids.append(post.get('id'))

print(post_ids)
