from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new')
def registeraccount():
    return render_template('register.html')


@app.route('/new/register',methods=['POST'])
def register():

    if not User.validate_register(request.form):
        return redirect('/new')
    data ={ 
        "username": request.form['username'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user_id'] = id

    return redirect('/dashboard')

@app.route('/login',methods=['POST'])
def login():
    user = User.get_by_email(request.form)

    if not user:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("dashboard.html",user=User.get_by_id(data),users=User.get_all())

@app.route('/edit/user/<int:id>')
def edit_user(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_user.html",edit=User.get_by_id(data),user=User.get_by_id(user_data))

@app.route('/update/user',methods=['POST'])
def update_user():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "username": request.form["username"],
        "email": request.form["email"],
        "id": request.form['id']
    }
    User.update(data)
    return redirect('/dashboard')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')