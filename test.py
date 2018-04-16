import requests

url = 'https://requestb.in/16b7rwv1'
json = {
    'tool': 'break',
    'reef': 'seek',
}
response = requests.post(url, params=json)
print(response.status_code)