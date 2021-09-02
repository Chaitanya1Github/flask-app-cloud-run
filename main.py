import os
from firebase_admin import firestore
from flask import Flask, jsonify, request, render_template
from werkzeug.utils import redirect
# from connection import db

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('home.html')

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']

        emp = {}

        emp['name'] = name
        if email != "":
            emp['email'] = email
        emp['phone'] = phone
        if address != "":
            emp['address'] = address

        # db.collection('emp_collection').add(emp)
        # return redirect('/read')
        return emp

    ################# when data comes in json form #################
    # data = request.get_json()
    # id = data['id']
    # db.collection('emp_collection').document(id).set(data)
    # return "alright"


'''
@app.route('/read', methods=['GET'])
def read():
    documents = db.collection('emp_collection').stream()
    employees = []
    for document in documents:
        emp = document.to_dict()
        emp['id'] = document.id
        employees.append(emp)
    return render_template('dashboard.html', employees=employees)


@app.route('/view/<id>', methods=['GET'])
def view(id):
    employee = db.collection('emp_collection').document(id).get()
    employee = employee.to_dict()
    return render_template('view.html', employee=employee)


@app.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'GET':
        employee = db.collection('emp_collection').document(id).get()
        employee = employee.to_dict()
        return render_template('update.html', employee=employee)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']

        emp = {
            "name": name,
            "email": email,
            "phone": phone,
            "address": address,
        }

        db.collection('emp_collection').document(id).update(emp)

        return redirect('/read')


@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    if request.method == 'GET':
        db.collection('emp_collection').document(id).delete()
        return redirect('/read')
'''


# @app.route('/delete/<id>', methods=['GET', 'POST'])
# def delete(id):
#     db.collection('emp_collection').document(id).delete()
#     return "document deleted"


port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=False, host='0.0.0.0', port=port)
