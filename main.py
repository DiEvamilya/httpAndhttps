import requests

url = "https://google.com"
a = requests.get(url)
a.raise_for_status()
print(a.text)