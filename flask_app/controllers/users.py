from flask import render_template, redirect, session
from flask_app import app
from flask_app.models import user, game, friend, users_game


# --- Dashboard ---
@app.route('/dashboard')
def dashboard():
    # display all games stored in database [PL]
        # from list of all games: can add/remove games to/from user's collection [HS]
        # from list of all games: can add/remove games to/from user's wishlist [HS]

    # display all games in user's wishlist and collection - via 'wishlist_games' and 'collection_games' [HS]

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

    # display all users - via 'all_users' [HS]
        # from list of all users: can add others to user's friend list - via 'add_friend' route

    # friends list
        # display all friends - via 'all_friends' [HS]
        # can remove others from user's friend list - via 'remove_friend' route [HS]

    return render_template('dashboard.html', all_users = user.User.get_all(), all_friends = friend.Friend.get_all_by_user(user_data), wishlist_games = users_game.UsersGame.get_users_games_by_status(wishlist_data), collection_games = users_game.UsersGame.get_users_games_by_status(collection_data))

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
def remove_friend(friend_id):
    data = {
        'user_id': session['user_id'],
        'friend_id': friend_id
    }

# --- Processes user's request to add game to collection or wishlist ---
@app.route('/add/<str:status>/game/<int:game_id>')
def add_to_game_category(status, game_id):
    data = {
        'user_id': session['user_id'],
        'game_id': game_id,
        'status': status
    }

    users_game.UsersGame.save(data)

    return redirect('/dashboard')

# --- Processes user's request to remove game from collection or wishlist ---
@app.route('/remove/<str:status>/game/<int:game_id>')
def remove_from_game_category(status, game_id):
    data = {
        'user_id': session['user_id'],
        'game_id': game_id,
        'status': status
    }

    users_game.UsersGame.delete(data)

    return redirect('/dashboard')