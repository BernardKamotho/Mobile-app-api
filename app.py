# we are using flask restful to create a rest api
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import pymysql

# creating a flask app

app = Flask(__name__)

# create an api object

api = Api(app)

class farmers(Resource):

    def put(self):
       data = request.json
       id_number = data['id_number']
       salary = data['salary']
       connection = pymysql.connect(host="localhost", user='root', password='', database='BenDB')
       cursor = connection.cursor()
       sql = "update employees SET salary = %s where id_number = %s"
       try:
           cursor.execute(sql,(id_number,salary))
           connection.commit()
           return jsonify({'message': "UPDATE SUCCESS"})
       except:
           connection.rollback()
           return jsonify({'message':"UPDATE FAILED"})
       
    
    def delete(self):
       data = request.json
       id_number = data['id_number']
       connection = pymysql.connect(host="localhost", user='root', password='', database='BenDB')
       cursor = connection.cursor()
       sql = "delete from employees where id_number = %s"
       try:
           cursor.execute(sql,(id_number))
           connection.commit()
           return jsonify({'message': "DELETE SUCCESS"})
       except:
           connection.rollback()
           return jsonify({'message':"DELETE FAILED"})

    
    def post(self):
         
        data = request.json
        id_number = data['id_number']
        username = data['username']
        others = data['others']
        salary = data['salary']
        department = data['department']

        connection = pymysql.connect(host="localhost", user='root', password='', database='BenDB')
        cursor = connection.cursor()
        sql = "insert into employees(id_number,username,others,salary,department) values(%s,%s,%s,%s,%s)"
        try:
            cursor.execute(sql,(id_number,username,others,salary,department))
            connection.commit()
            return jsonify({'message': 'POST SUCCESS'})
        except:
            connection.rollback()
            return jsonify({'message': 'POST FAILED'})   


    def get(self):
        connection = pymysql.connect(host="localhost", user='root', password='', database='BenDB')
        cursor = connection.cursor()
        sql = "select  * from employees"
        cursor.execute(sql)
        if cursor.rowcount == 0:
            return jsonify({'message': 'NO RECORD FOUND'})
        else:
            employeesdata = cursor.fetchall()
            return jsonify(employeesdata)


        return jsonify({"message":"hey Bernard post to the bendb was a success"})
    
api.add_resource(Employee, "/employees")

if __name__== "__main__":
    app.run(debug=True)
