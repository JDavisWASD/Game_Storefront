from flask import redirect, render_template, session
from flask_app import app
from flask_app.models import friend, game, users_game, user


@app.route('/view/game/<int:game_id>')
def view_game(game_id):
    if 'user_id' not in session:
        return redirect('/login')

    collection = {
        'user_id': session['user_id'],
        'game_id': game_id,
        'status': 'collection'
    }

    wishlist = {
        'user_id': session['user_id'],
        'game_id': game_id,
        'status': 'wishlist'
    }

    data ={
        'user_id': session['user_id']
    }

    game_data = {
        'game_id': game_id
    }

    user_game_data = {
        'user_id': session['user_id'],
        'game_id': game_id
    }

    return render_template('game.html', game = game.Game.get_by_id(game_data), \
        friends_collection = friend.Friend.get_friends_games(collection), \
        friends_wishlist = friend.Friend.get_friends_games(wishlist), \
        self_user = user.User.get_by_id(data), \
        all_games = game.Game.get_all(), all_users = user.User.get_all(),
        status_games = users_game.UsersGame.get_user_game_status(user_game_data))

# --- Processes user's request to add game to collection or wishlist ---
@app.route('/add/<status>/game/<int:game_id>')
def add_status(status, game_id):
    data = {
        'user_id': session['user_id'],
        'game_id': game_id,
        'status': status
    }

    users_game.UsersGame.save(data)

    return redirect('/dashboard')

# --- Processes user's request to change status from wishlist to collection ---
@app.route('/update/<status>/game/<int:game_id>')
def update_status(status, game_id):
    data = {
        'user_id': session['user_id'],
        'game_id': game_id,
        'status': status
    }

    users_game.UsersGame.update(data)

    return redirect('/dashboard')