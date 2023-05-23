from flask import *
from flask_restful import Resource,Api
app=Flask(__name__)
import pymysql
# create the Api Objevt
api=Api(app)
 

class Signup(Resource):
    # define the function for the 4 HTTP methods (POST,GET,PUT,DELETE)
    # the 4 methods are automatically mapped by flask_restful
    def post(self): #POST
        # Json format
        data=request.json
        # id_number, username,others,salary,department
        farmername=data['farmername']
        id_number=data['id_number']
        location=data['location']
        phonenumber=data['phonenumber']
        password1=data['password']
        password2=data['password2']
 
        if len(password1) < 8:
 
            return jsonify({'message':'Password must be more than 8 xters'})
 
            # Check if the 2 passwords are matching, if not notify the user to match them up.
        elif password1 != password2:
 
            return jsonify({'message':'Password do not match'})
        else:
            connection=pymysql.connect(host="localhost",user="root                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ",password="",database="farmers")
 
            # create cursor
 
            cursor=connection.cursor()
            # define the sql query
            sql="insert into users (farmername,id_number,location,phonenumber,password) values(%s,%s,%s,%s,%s)"
            # try and except
            # try:
            cursor.execute(sql,(farmername,id_number,location,phonenumber,password1,password2))
            connection.commit()
            response=jsonify({"message":"registration successful"})
            response.status_code=200
            return response
            # except:
            #     connection.rollback()
            #     response=jsonify({"message":"Failed. User Not Saved"})
            #     response.status_code=500
            #     return response
 
api.add_resource(Signup,"/signup")