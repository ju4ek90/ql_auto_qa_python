import requests

requests_url = 'https://inweb.ua/seo'

r = requests.get(requests_url, allow_redirects=False)
if r.status_code == 301:
    print('For url ', r.url, ' status code is ', r.status_code, ' Redirected to ', r.headers['Location'])
    r = requests.get(r.headers['Location'], allow_redirects=False)
print('For url ', r.url, ' status code is ', r.status_code)
