from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

class Friend:
    DATABASE = 'game_platform'

    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.friend_id = data['friend_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#Get functions -----------------------------------------------------------------
    @classmethod
    def get_all_by_user(cls, data):
        query = 'SELECT * FROM friends JOIN users ON friend_id = users.id ' \
            'WHERE user_id = %(user_id)s;'
        results = connectToMySQL(cls.DATABASE).query_db(query, data)
        friends = []
        for row in results:
            user_data = {
                'id': row['friend_id'],
                'username': row['username'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            friends.append(user.User(user_data))

        return friends

    @classmethod
    def get_one_by_ids(cls, data):
        query = 'SELECT * FROM friends WHERE user_id = %(user_id)s AND ' \
            'friend_id = %(friend_id)s;'
        result = connectToMySQL(cls.DATABASE).query_db(query, data)
        if result:
            return cls(result[0])

        return False

    @classmethod
    def get_friends_games(cls, data):
        query = 'SELECT * FROM friends JOIN users ON users.id = friend_id ' \
            'JOIN users_games ON users_games.user_id = friend_id WHERE ' \
            'friends.user_id = %(user_id)s AND game_id = %(game_id)s AND ' \
            'status = %(status)s;'
        results = connectToMySQL(cls.DATABASE).query_db(query, data)
        friends = []
        for row in results:
            user_data = {
                'id': row['friend_id'],
                'username': row['username'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            friends.append(user.User(user_data))

        return friends

#Modify functions --------------------------------------------------------------
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO friends (user_id, friend_id, created_at, ' \
            'updated_at) VALUES (%(user_id)s, %(friend_id)s, NOW(), NOW());'
        connectToMySQL(cls.DATABASE).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM friends WHERE user_id = %(user_id)s AND ' \
            'friend_id = %(friend_id)s;'
        connectToMySQL(cls.DATABASE).query_db(query, data)