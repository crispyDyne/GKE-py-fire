import os

from flask import Flask, request

import firebase_admin 
from firebase_admin import firestore, db
import time



############
## YOUR REALTIME DATABASE ADDRESS GOES HERE!!! #####
dbAddress = 'https://[projectID].firebaseio.com/'
###########



# initialize the firebase SDK
cred = None # the service account should provide the credentials
firebase_admin.initialize_app(cred,options ={'databaseURL': dbAddress})

# get firestore client 
fs = firestore.client()

app = Flask(__name__)

@app.route('/')
def hello_world():
    print('Hello, World print statement!')
    return 'Hello, World!'

@app.route('/simplepost', methods = ['POST'])
def simple_post():
    content = request.get_json()
    return {'results': content}, 201

@app.route('/firepost', methods = ['POST'])
def fire_post():
    jobRef = db.reference('jobs/').push()
    return {'results': jobRef.path}, 201

@app.route('/storepost', methods = ['POST'])
def store_post(): 
    doc = fs.collection('junk').add({"more":'trash'})
    return {'results': doc[1].path}, 201

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))