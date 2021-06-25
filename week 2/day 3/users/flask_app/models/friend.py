from flask_app.config.mysqlconnection import connectToMySQL

class Friend:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        results = connectToMySQL('first_flask').query_db(query)
        friends = []
        for friend in results:
            friends.append( cls(friend) )
        return friends


    @classmethod
    def save(cls, data ):
        query = "INSERT INTO friends ( first_name , last_name , occupation , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(occ)s , NOW() , NOW() );"
        print("Hello")
        return connectToMySQL('first_flask').query_db( query, data )


    @classmethod
    def display_friend(cls, data):
        query = "SELECT * FROM friends WHERE id = %(id)s;"
        results = connectToMySQL('first_flask').query_db(query, data)
        return results[0]


    @classmethod
    def delete(cls, data):
        query = "DELETE FROM friends WHERE id = %(id)s;"
        connectToMySQL('first_flask').query_db(query, data)

    
    @classmethod
    def update(cls, data):
        query = "UPDATE friends SET first_name = %(fname)s, last_name = %(lname)s, occupation = %(occ)s, updated_at = NOW() WHERE id = %(id)s;"
        results =connectToMySQL('first_flask').query_db(query, data)
        print(results)
        return results