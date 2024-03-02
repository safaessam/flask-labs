from flask import Flask, request, render_template, redirect
app = Flask(__name__)

users = [
    {"id": 1, "name": "mina", "age": 30, "location": "giza"},
    {"id": 2, "name": "fatma", "age": 30, "location": "cairo"}
]

def get_next_id():
    if len(users) > 0:
        return users[-1]['id'] + 1
    else:
        return 1

@app.route('/')
def home():
    return render_template('home.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    name = request.form.get('name')
    age = request.form.get('age')
    location = request.form.get('location')

    if name and age and location:
        users.append({"id": get_next_id(), "name": name, "age": age, "location": location})

    return redirect('/')

@app.route('/delete/<int:id>', methods=['POST'])
def delete_user(id):
    for i, user in enumerate(users):
        if user['id'] == id:
            del users[i]
            break

    return redirect('/')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        location = request.form.get('location')

        for user in users:
            if user['id'] == id:
                user['name'] = name
                user['age'] = age
                user['location'] = location
                break

        return redirect('/')
    else:
        user = None
        for u in users:
            if u['id'] == id:
                user = u
                break

        return render_template('edit.html', user=user)