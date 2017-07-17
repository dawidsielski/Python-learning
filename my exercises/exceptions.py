import requests

def get_response(url):
    return requests.get(url)



if __name__ == "__main__":
    resp = requests.Response()
    try:
        resp = get_response('https://jsonplaceholder.typicode.com/posts/asd')
    except requests.ConnectionError as connection_error:
        print(connection_error)
    print(resp.text)