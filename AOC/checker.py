import requests
import json
import urllib


url = "https://medium.com/tag/bauen"

file = requests.get(url=url)
print(file.text)
