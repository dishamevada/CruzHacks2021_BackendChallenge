from flask import Flask, request, jsonify, json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#UPDATE WITH YOUR OWN PATH
cred = credentials.Certificate('/Users/dishamevada/hacker-docs-firebase-adminsdk-gg8v0-30ed747e43.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

app = Flask(__name__)

@app.route('/getHackerInfo', methods=['POST', 'PUT', 'GET'])
def gethackerinfo():
    #creates nameID to identify documents
    hacker_data_raw = request.data
    my_json_str = hacker_data_raw.decode('utf8').replace("'", '"')
    hacker_data = json.loads(my_json_str)

    firstName = hacker_data.get("firstName")
    lastName = hacker_data.get("lastName")
    nameID = firstName + " " + lastName

    if request.method == 'GET':
        users_ref = db.collection(u'users')
        docs = users_ref.stream()

        # print(u'{} => {}'.format(doc.id, doc.to_dict()))
        for doc in docs:
            if doc.id == nameID:
                #result = '{"code": 200, "message": "Succesful retrieve from database"}'
                #Returns content
                return doc.to_dict()
        result = '{"code": 400, "message": "Unable to retrive user from database"}'
        return jsonify(result)


    if request.method == 'POST':
        doc_ref = db.collection(u'users').document(nameID)
        doc_ref.set(hacker_data)
        result = '{"code": 200, "message": "Succesful post to database"}'
        return jsonify(result)

    #Does not fully work
    if request.method == 'PUT':
        doc_ref = db.collection(u'users').document(nameID)
        doc_ref.update(hacker_data)
        result = '{"code": 200, "message": "Succesful update to database"}'
        return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=8085, host="0.0.0.0")