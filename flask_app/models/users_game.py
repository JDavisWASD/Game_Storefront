from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import game
from flask_app.models import user

class UsersGame:
    DATABASE = 'game_platform'

    def __init__(self, data):
        self.user_id = data['user_id']
        self.game_id = data['game_id']
        self.status = data['status']    #'collection' or 'wishlist' only
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#Get functions -----------------------------------------------------------------
    @classmethod
    def get_users_games_by_status(cls, data):
        query = 'SELECT * FROM users_games JOIN games ON game_id = games.id ' \
            'WHERE user_id = %(user_id)s AND status = %(status)s;'
        results = connectToMySQL(cls.DATABASE).query_db(query, data)
        games = []
        for row in results:
            game_data = {
                'id': row['game_id'],
                'name': row['name'],
                'genre': row['genre'],
                'release_date': row['release_date'],
                'price': row['price'],
                'image_source': row['image_source'],
                'description': row['description'],
                'created_at': row['games.created_at'],
                'updated_at': row['games.updated_at']
            }
            games.append(game.Game(game_data))

        return games    # returns a list called 'games'

    @classmethod
    def get_users_by_game(cls, data):
        query = 'SELECT * FROM users_games JOIN users ON user_id = users.id ' \
            'WHERE game_id = %(game_id)s;'
        results = connectToMySQL(cls.DATABASE).query_db(query, data)
        users = []
        for row in results:
            user_data = {
                'id': row['users_id'],
                'username': row['username'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            users.append(user.User(user_data))

        return users    # returns a list called 'users'

    @classmethod
    def get_user_game_status(cls,data):
        query ='SELECT * FROM users_games WHERE game_id = %(game_id)s AND user_id = %(user_id)s;'
        results = connectToMySQL(cls.DATABASE).query_db(query, data)
        status = []
        if len(results) == 0: status=[] 
        else: status.append((results[0]))
        return status

#Modify functions --------------------------------------------------------------
    @classmethod
    def save(cls, data):
        if data['status'].lower() != 'collection' and \
                data['status'].lower() != 'wishlist':
            print('Error: Status must be "collection" or "wishlist".')
            return False

        query = 'INSERT INTO users_games (user_id, game_id, status, ' \
            'created_at, updated_at) VALUES (%(user_id)s, %(game_id)s, ' \
            '%(status)s, NOW(), NOW());'
        connectToMySQL(cls.DATABASE).query_db(query, data)

    @classmethod
    def update(cls, data):
        if data['status'].lower() != 'collection' and \
                data['status'].lower() != 'wishlist':
            print('Error: Status must be "collection" or "wishlist".')
            return False

        query = 'UPDATE users_games SET status = %(status)s, ' \
            'updated_at = NOW() WHERE user_id = %(user_id)s AND ' \
            'game_id = %(game_id)s;'
        connectToMySQL(cls.DATABASE).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM users_games WHERE user_id = %(user_id)s AND ' \
            'game_id = %(game_id)s AND status = %(status)s;'
        connectToMySQL(cls.DATABASE).query_db(query, data)