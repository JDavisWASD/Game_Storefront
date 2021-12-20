from flask import redirect, session
from flask_app import app

@app.route('/view/<int:game_id>')
def view_game(game_id):
    if 'user_id' not in session:
        return redirect('/login')

    pass