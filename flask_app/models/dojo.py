#Import the function that will return the Instance of connection
from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninjas
# model the class after the dojo table from our database
class Dojos:
    def __init__(self,data) -> None:
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.ninjas=[]
        # Now we use class methods to query our database
    # Retrieve Data from table using select query
    @classmethod
    def get_all(cls):
        query= "SELECT * FROM dojos;"
    # make sure to call the connectToMySQL function with the schema you are targeting.
        results=connectToMySQL("dojos_and_ninjas").query_db(query)
        # create an empty list to append our instances of dojos
        dojos=[]
        # Iterate over the db results and create instances of user with cls
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    # Insert into dojo table using Insert query
    @classmethod
    def save(cls,data):
        query="Insert INTO dojos(name)values(%(name)s);"
        return connectToMySQL("dojos_and_ninjas").query_db(query,data)

    # Getting only one location from the list or the table
    @classmethod
    def get_one(cls,data):
        query="SELECT * FROM dojos LEFT JOIN ninjas on dojos.id=ninjas.dojos_id WHERE dojos.id=%(id)s;"
        result= connectToMySQL('dojos_and_ninjas').query_db(query,data)
        print("Result is ",result)
        dojo = cls(result[0])
        print("result[0] =",result[0])
        print("dojo is",dojo)
        for row in result:
            n = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            print("id is",n['id'],"NAME IS ",n['first_name'] )
            print(Ninjas(n))
            dojo.ninjas.append( Ninjas(n) )
        return dojo