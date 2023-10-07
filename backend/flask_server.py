'''
Created on Aug 21, 2023

@author: daniel
'''
from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
from db_manager import DbManager
from pdf_generator import pdfGenerator
import requests
import os
import json

SECRET = ''

backend_dir = os.getcwd()
project_dir = os.path.dirname(backend_dir)
secret_file = os.path.join(project_dir, 'secret.txt')

with open(secret_file) as config_file:
    config = json.load(config_file)
    SECRET = config.get('INTELLISPHERE_SECRET')


app = Flask(__name__)

DB_MANAGER = DbManager()
#DB_MANAGER.addAlunno({'name': 'Giorgio', 'age': 30, 'additional_req': ' con solo moltiplicazioni'})
#DB_MANAGER.addAlunno({'name': 'Luca', 'age': 20, 'additional_req': ' con solo addizioni'})


# Define a route that returns some values
@app.route('/is_alive')
def is_alive():
    SESSION_ID = login_chat_gpt()
    response = {'result': SESSION_ID}
    return jsonify(response)

@app.route('/search_text', methods=['GET'])
def search_text():
    all_text = request.args.get('all_text')
    alunno_id = request.args.get('alunno_id')
    merge = request.args.get('merge')
    if not all_text:
        return jsonify({'error': 'Missing parameters'}), 400
    SESSION_ID = login_chat_gpt()
    
    out = {}
    
    if alunno_id:
        alunni = DB_MANAGER.getAunnoById(int(alunno_id))
    else:
        alunni = DB_MANAGER.getAlunni()
    
    all_pdf = []
    for alunno in alunni:
        result = submitChatGPT(SESSION_ID, all_text + alunno.additional_req)
        
        out.setdefault(alunno.id, {})
        out[alunno.id]['txt_res'] = "%s\n\n" % (alunno.name.capitalize()) + result
        new_pdf = pdfGenerator('%s.pdf' % (alunno.name), out[alunno.id]['txt_res'])
        out[alunno.id]['pdf_res'] = new_pdf.generate_pdf()
        all_pdf.append(out[alunno.id]['pdf_res'])
        
    if merge:
        new_pdf = pdfGenerator('merged.pdf', out[alunno.id]['txt_res'])
        out.setdefault('all', {'txt_res': '',
                               'pdf_res': new_pdf.pdf_merge(all_pdf)
                               })
    return jsonify({'result': result})



def login_chat_gpt():
    url = 'https://backend.memori.ai/memori/v2/session'
    data = {
        "memoriId": SECRET,
        "password": "undefined",
        "birthDate": "1986-04-24T13:38:07.728Z"
    }
    headers={
        'Content-Type': 'application/json'
        }
    response = requests.post(url, data=json.dumps(data), headers=headers)
    
    if response.status_code == 200:
        SESSION_ID = json.loads(response.text).get('sessionID')
        #print('Response:', response.text)
    else:
        print('Request failed with status code:', response.status_code)
    return SESSION_ID

def submitChatGPT(session_id, question):
    url = 'https://backend.memori.ai/memori/v2/TextEnteredEvent/' + session_id
    
    data = {
        "text": question
    }
    
    headers={
        'Content-Type': 'application/json'
        }
    response = requests.post(url, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        emission = json.loads(response.text).get('currentState', {}).get('emission')
        print('Response:', response.text)
    else:
        print('Request failed with status code:', response.status_code)
    return emission

if __name__ == '__main__':
    app.run(debug=True)
