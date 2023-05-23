from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import pymysql
app = Flask(__name__)
api = Api(app)

class Farmers(Resource):

    def post(self):
        data = request.json
        farmer_id = data['farmer_id']
        farmer_name = data['farmer_name']
        farmer_location = data['farmer_location']
        earnings = data['earnings']
    
        connection = pymysql.connect(host="localhost", user='root', password='', database='PaaEmpDB')
        cursor = connection.cursor()
        sql = "insert into farmers(farmer_id,farmer_name,farmer_location,earnings) values(%s,%s,%s,%s)"
        try:
            cursor.execute(sql,(farmer_id,farmer_name,farmer_location,earnings))
            connection.commit()
            return jsonify({'message': 'POST SUCCESS'})
        except:
            connection.rollback()
            return jsonify({'message': 'POST FAILED'}) 

    def get(self):
        connection = pymysql.connect(host="localhost", user='root', password='', database='PaaEmpDB')
        cursor = connection.cursor()
        sql = "select  * from farmers"
        cursor.execute(sql)
        if cursor.rowcount == 0:
            return jsonify({'message': 'NO RECORD FOUND'})
        else:
            farmersdata = cursor.fetchall()
            return jsonify(farmersdata) 
        
       

api.add_resource(Farmers, "/farmers")

if __name__== "__main__":
    app.run(debug=True) 
