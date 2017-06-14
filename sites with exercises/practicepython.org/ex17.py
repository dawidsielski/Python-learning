import requests

url = 'http://www.github.com'
r = requests.get(url)
r_html = r.text

print(r_html)
