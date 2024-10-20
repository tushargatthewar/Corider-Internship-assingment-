from flask import Blueprint, render_template, request, redirect, url_for
from bson.objectid import ObjectId

main = Blueprint('main', __name__)

@main.route('/')
def index():
    users = main.current_app.db['tableofuser'].find()
    return render_template('index.html', users=users)

@main.route('/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        if name and email and password:
            main.current_app.db['tableofuser'].insert_one({'name': name, 'email': email, 'password': password})
            return redirect(url_for('main.index'))
        else:
            return "Missing required fields", 400

    return render_template('create_user.html')

@main.route('/update/<id>', methods=['GET', 'POST'])
def update_user(id):
    user = main.current_app.db['tableofuser'].find_one({'_id': ObjectId(id)})
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        if name and email and password:
            main.current_app.db['tableofuser'].update_one(
                {'_id': ObjectId(id)},
                {'$set': {'name': name, 'email': email, 'password': password}}
            )
            return redirect(url_for('main.index'))
        else:
            return "Missing required fields", 400

    return render_template('update_user.html', user=user)

@main.route('/delete/<id>')
def delete_user(id):
    main.current_app.db['tableofuser'].delete_one({'_id': ObjectId(id)})
    return redirect(url_for('main.index'))
