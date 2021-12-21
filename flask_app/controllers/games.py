from flask import redirect, render_template, session
from flask_app import app
from flask_app.models import game

@app.route('/view/<int:game_id>')
def view_game(game_id):
    if 'user_id' not in session:
        return redirect('/login')

    return render_template('game.html')