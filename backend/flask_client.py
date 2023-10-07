'''
Created on Aug 21, 2023

@author: daniel
'''
import requests
import json

# url = 'http://127.0.0.1:5000/is_alive'
# response = requests.get(url)
#
# if response.status_code == 200:
#     values = response.json()
#     print("Received values:", values)
# else:
#     print("Error:", response.status_code)
    
    


url = 'http://127.0.0.1:5000/search_text'
data = {
    "all_text": "Chi ha vinto il campionato di Serie A l'hanno scorso?",
    }
response = requests.get(url, params=data)

if response.status_code == 200:
    values = response.json()
    print("Received values:", values.get('result'))
else:
    print("Error:", response.status_code)