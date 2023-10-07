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
    
    


# url = 'http://127.0.0.1:5000/search_text'
# data = {
#     "all_text": "genera un quiz a crocette come test di ingresso di prima superiore.",
#     "alunno_id": 1
#     }
# response = requests.get(url, params=data)
#
# if response.status_code == 200:
#     values = response.json()
#     print("Received values:", values.get('result'))
# else:
#     print("Error:", response.status_code)
    
    
url = 'http://127.0.0.1:5000/get_students'
data = {
    "alunno_id": 1
    }
response = requests.get(url, params=data)

if response.status_code == 200:
    values = response.json()
    print("Received values:", values.get('result'))
else:
    print("Error:", response.status_code)
    