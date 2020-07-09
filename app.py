import os

from flask import Flask, request

import firebase_admin 
from firebase_admin import credentials, db

app = Flask(__name__)



############
## YOUR REALTIME DATABASE ADDRESS GOES HERE!!! #####
dbAddress = 'https://[projectID].firebaseio.com/'
###########



# initialize the firebase SDK
credentials = None # the service account should provide the credentials
# credentials = firebase_admin.credentials.ApplicationDefault() # same behavior
fire = firebase_admin.initialize_app(credentials,{'databaseURL': dbAddress})

@app.route('/')
def hello_world(): # works on cloud run and GKE
    print('Hello, World print statement!')
    return 'Hello, World!'

@app.route('/simplepost', methods = ['POST'])
def simple_post():# works on cloud run and GKE
    content = request.get_json()
    return {'results': content}, 201

@app.route('/firepost', methods = ['POST'])
def fire_post(): # works on cloud run. FAILS ON GKE!
    jobRef = db.reference('jobs/').push()
    return {'results': jobRef.path}, 201

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))