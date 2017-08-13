import requests

URL = 'https://jsonplaceholder.typicode.com/posts'

req = requests.get(URL)
print(req)
# print(req.text) # gives str object
# print(req.content) # gives binary object
print(req.headers)
print(req.url)
print(req.encoding)
print(req.json())

print("=" * 40)

payload = {'id': '1'}
req_with_payload = requests.get(URL, params=payload)
print(req_with_payload)
print(req_with_payload.url)
print(req_with_payload.json())

print("=" * 40)

req_with_timeout = requests.get(URL, timeout=0.1)
print(req_with_timeout)

print("=" * 40)

github_request = requests.get('http://github.com', allow_redirects=False)
print(github_request)
print(github_request.status_code)
print(github_request.history)
