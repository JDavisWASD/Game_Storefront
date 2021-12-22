from flask import flash, redirect, render_template, request, session
from flask_app import app
from flask_app.models import user, game, friend, users_game
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# --- Landing page - includes login ---
@app.route('/')
def index():
    return render_template('index.html')

# --- Register page ---
@app.route('/new')
def registeraccount():
    return render_template('register.html')

# --- Processes user input to create a new user
@app.route('/new/register',methods=['POST'])
def register():
    if not user.User.validate_new_user(request.form):
        return redirect('/new')
    data ={ 
        "username": request.form['username'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = user.User.save(data)
    session['user_id'] = id

    return redirect('/dashboard')

# --- Processes login info ---
@app.route('/login',methods=['POST'])
def login():
    found_user = user.User.get_by_email(request.form)

    if not found_user:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(found_user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/')
    session['user_id'] = found_user.id
    return redirect('/dashboard')

# --- Dashboard ---
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')

    user_data = {
        'user_id': session['user_id']
    }

    wishlist_data = {
        'user_id': session['user_id'],
        'status': "wishlist"
    }

    collection_data = {
        'user_id': session['user_id'],
        'status': "collection"
    }
    users = user.User.get_all()
    friends = friend.Friend.get_all_by_user(user_data)
    friends_index = {}

    #Record the index of a person in friends list into a dictionary accessable by
    #that persons user_id
    for usr in users:
        for i in range(len(friends)):
            if usr.id == friends[i].id:
                friends_index[usr.id] = i

    return render_template('dashboard.html', \
        self_user = user.User.get_by_id(user_data), \
        all_games = game.Game.get_all(), all_users = users, \
        all_friends = friends, index = friends_index, \
        wishlist_games = users_game.UsersGame.get_users_games_by_status(wishlist_data), \
        collection_games = users_game.UsersGame.get_users_games_by_status(collection_data))

# --- Processes user's request to add another user to friends list ---
@app.route('/add/friend/<int:friend_id>')
def add_friend(friend_id):
    data = {
        'user_id': session['user_id'],
        'friend_id': friend_id
    }

    friend.Friend.save(data)

    return redirect('/dashboard')

# --- Processes user's request to add another user to friends list ---
@app.route('/remove/friend/<int:friend_id>')
def remove_friend(friend_id):
    data = {
        'user_id': session['user_id'],
        'friend_id': friend_id
    }

    friend.Friend.delete(data)

    return redirect('/dashboard')

# --- Processes user's request to remove game from collection or wishlist ---
@app.route('/remove/<status>/game/<int:game_id>')
def remove_from_game_category(status, game_id):
    data = {
        'user_id': session['user_id'],
        'game_id': game_id,
        'status': status
    }

    users_game.UsersGame.delete(data)

    return redirect('/dashboard')

# --- Edit account settings page
@app.route('/edit')
def edit_user():
    if 'user_id' not in session:
        return redirect('/')

    data = {'user_id': session['user_id']}
    return render_template('edit.html', user = user.User.get_by_id(data))

@app.route('/update_user', methods = ['POST'])
def update_user():
    data = {
        'user_id': session['user_id'],
        'username': request.form['username'],
        'email': request.form['email']
    }
    if not user.User.validate_update(data):
        return redirect('/edit')

    user.User.update(data)
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/')
