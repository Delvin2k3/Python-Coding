import requests
from rich import print

z = requests.get('https://www.apple.com/')
print(z.text)  