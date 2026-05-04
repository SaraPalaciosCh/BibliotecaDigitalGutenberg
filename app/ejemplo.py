import re
import requests
try:
    resp_error = requests.get('https://www.tu_pagina.com/')
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print(e)

resp_404 = requests.get('https://www.gutenberg.org/cache/epub/846552564156/pg84.txt')
resp_200 = requests.get('https://www.gutenberg.org/cache/epub/84/pg84.txt')
print(resp_404.status_code)
print(type(resp_404.status_code))

m = re.search(r'(Author:)\s+\w+.+\n', resp_200.text)
print(m.group(0))

