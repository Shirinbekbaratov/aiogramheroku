import requests

response=requests.get('https://v6.exchangerate-api.com/v6/9ea72025e6fd3b212e18f573/pair/USD/UZS').json()
print(response['conversion_rate'])