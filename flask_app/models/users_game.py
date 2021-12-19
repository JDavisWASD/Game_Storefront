from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import game
from flask_app.models import user

class UsersGame:
    DATABASE = 'game_platform'

    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.game_id = data['game_id']
        self.status = data['status']    #'owned' or 'wishlist' only
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#Get functions -----------------------------------------------------------------
    @classmethod
    def get_users_games_by_status(cls, data):
        query = 'SELECT * FROM users_games JOIN games on game_id = games.id ' \
            'WHERE user_id = %(user_id)s AND status = %(status)s;'
        results = connectToMySQL(cls.DATABASE).query_db(query, data)
        games = []
        for row in results:
            game_data = {
                'id': row['games.id'],
                'name': row['name'],
                'genre': row['genre'],
                'release_date': row['release_date'],
                'price': row['price'],
                'description': row['decription'],
                'created_at': row['games.created_at'],
                'updated_at': row['games.updated_at']
            }
            games.append(game.Game(game_data))

        return games

    @classmethod
    def get_users_by_game(cls, data):
        query = 'SELECT * FROM users_games JOIN users on user_id = users.id ' \
            'WHERE game_id = %(game_id)s;'
        results = connectToMySQL(cls.DATABASE).query_db(query, data)
        users = []
        for row in results:
            user_data = {
                'id': row['users.id'],
                'username': row['username'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            users.append(user.User(user_data))

        return users

#Modify functions --------------------------------------------------------------
    @classmethod
    def save(cls, data):
        if data['status'].lower() != 'owned' and \
                data['status'].lower() != 'wishlist':
            print('Error: Status must be "owned" or "wishlist".')
            return False

        query = 'INSERT INTO users_games (user_id, game_id, status, ' \
            'created_at, updated_at) VALUES (%(user_id)s, %(game_id)s, ' \
            '%(status)s, NOW(), NOW());'
        return connectToMySQL(cls.DATABASE).query_db(query, data)

    @classmethod
    def update(cls, data):
        if data['status'].lower() != 'owned' and \
                data['status'].lower() != 'wishlist':
            print('Error: Status must be "owned" or "wishlist".')
            return False

        query = 'UPDATE users_games SET status = %(status)s WHERE ' \
            'user_id = %(user_id)s AND game_id = %(game_id)s;'
        connectToMySQL(cls.DATABASE).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM users_games WHERE user_id = %(user_id)s AND ' \
            'game_id = %(game_id)s;'
        connectToMySQL(cls.DATABASE).query_db(query, data)