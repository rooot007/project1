import requests

url = 'https://requestb.in/1d2kiws1'
json = {
    'tool': 'break',
    'reef': 'seek',
}
response = requests.post(url, json= json)
print(response.status_code)