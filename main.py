import requests

url = "https://yh-finance.p.rapidapi.com/auto-complete"

querystring = {"q":"tesla","region":"US"}

headers = {
    'x-rapidapi-host': "yh-finance.p.rapidapi.com",
    'x-rapidapi-key': "b4a4adc81cmsh8de444c388a3787p1de398jsn8e04e7775728"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)