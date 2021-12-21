from flask_app.config.mysqlconnection import connectToMySQL

class Game:
    DATABASE = 'game_platform'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.genre = data['genre']
        self.release_date = data['release_date']
        self.price = data['price']
        self.image_source = data['image_source']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#Get functions -----------------------------------------------------------------
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM games;'
        results = connectToMySQL(cls.DATABASE).query_db(query)
        games = []
        for row in results:
            games.append(cls(row))

        return games

    @classmethod
    def get_by_id(cls, data):
        query = 'SELECT * FROM games WHERE id = %(game_id)s;'
        result = connectToMySQL(cls.DATABASE).query_db(query, data)
        if result:
            return cls(result[0])

        return False