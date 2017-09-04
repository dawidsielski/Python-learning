import requests
import json


url = 'https://jsonplaceholder.typicode.com/posts'

try:
    req = requests.get(url)
except Exception as error :
    print(error)


print(req.status_code)
# print(req.text)

posts_data = json.loads(req.text)
print(posts_data[0])