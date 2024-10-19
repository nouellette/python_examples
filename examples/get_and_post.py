import requests

res = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
# print(res.json())


data = requests.post('https://httpbin.org/post', data={'haha': 'test'})
print(data.json())