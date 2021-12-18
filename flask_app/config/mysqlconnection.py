import pymysql.cursors

class MySQLConnection:
    def __init__(self, db):
        connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = 'root',
            db = db,
            charset = 'utf8mb4',
            cursorclass = pymysql.cursors.DictCursor,
            autocommit = True
        )
        self.connection = connection

    def query_db(self, query, data = None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)

                cursor.execute(query, data)

                #INSERT will return ID number of the inserted row
                if query.lower().find("insert") >= 0:
                    self.connection.commit()
                    return cursor.lastrowid

                #SELECT will return the data as a list of dictionaries
                elif query.lower().find("select") >= 0:
                    result = cursor.fetchall()
                    return result

                #UPDATE and DELETE will return nothing
                else:
                    self.connection.commit()

            #If the query fails the method will return False
            except Exception as error:
                print("Something went wrong", error)
                return False
            finally:
                self.connection.close()

def connectToMySQL(db):
    return MySQLConnection(db)