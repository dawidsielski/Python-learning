import requests

url = 'https://jsonplaceholder.typicode.com/posts'

try:
    req = requests.get(url)
except Exception as error :
    print(error)


print(req.status_code)
print(req.text)