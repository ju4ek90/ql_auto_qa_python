import requests

r = requests.get('https://google.com')
print(r.status_code)
print(r.headers)


def is_status_code_equals(url, status_code):
    r = requests.get(url)
    return r.status_code == status_code


print(is_status_code_equals('https://google.com', 200))
