import mysql.connector
from flask import Flask,jsonify,request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

connection=mysql.connector.connect(
    host='localhost',
    user='root',
    password='rajesh',
    database='new_db'
)

cursor=connection.cursor()

@app.route('/employee', methods=['POST'])
def add_user():
    data=request.json
    name=data['name']
    id=data['id']
    age=data['age']
    department=data['department']
    email=data['email']
    gender=data['gender']
    salary=data['salary']

    cursor.execute('insert into employee(name,id,age,department,email,gender,salary) values (%s,%s,%s,%s,%s,%s,%s)',(name,id,age,department,email,gender,salary))
    connection.commit()
    return jsonify({"message":"employee added successfully"}), 201

@app.route('/employee/<int:id>',methods=['GET'])
def get_emp_ById(id):
    cursor.execute("select * from employee where id=%s",(id,))
    result=cursor.fetchone()

    if result:
        return jsonify(result)

    else:
        return jsonify({'message':"employee not found"})
    

@app.route('/employee',methods=['GET'])
def get_allemp():
    
    cursor.execute("SELECT * from employee")
    result=cursor.fetchall()
    return jsonify(result)
    


@app.route('/employee/department/<string:department>',methods=['GET'])
def get_emp_ByDepartment(department):
    cursor.execute("select * from employee where department=%s",(department,))
    result=cursor.fetchall()

    if result:
        return jsonify(result)

    else:
        return jsonify({'message':"employee not found"})
    


@app.route('/employee/<string:gender>',methods=['GET'])
def get_emp_ByGender(gender):
    cursor.execute("select * from employee where gender=%s",(gender,))
    result=cursor.fetchall()

    if result:
        return jsonify(result)

    else:
        return jsonify({'message':"employee not found"})
    
@app.route('/employee/<int:id>',methods=['DELETE'])
def delete_employee(id):
    cursor.execute('delete from employee where id=%s',(id,))
    connection.commit()
    return jsonify({"message":"deleted successfully"})

@app.route('/employee/<int:id>', methods=['PUT'])
def update_employee(id):
    data=request.json
    name=data['name']
    age=data['age']
    department=data['department']
    email=data['email']
    gender=data['gender']
    salary=data['salary']
    cursor.execute('update employee set name=%s,age=%s,department=%s,email=%s,gender=%s,salary=%s where id=%s',(name,age,department,email,gender,salary,id))
    connection.commit()
    return jsonify({"message": "User updated successfully"})
@app.route('/employee/count',methods=['GET'])
def count_employee():
    cursor.execute("select count(id) from employee")
    result = cursor.fetchone()  # fetches a single value (count)
    
    if result:
        return jsonify({"employee_count": result})  # Returning count as JSON
    else:
        return jsonify({"message": "Could not retrieve employee count"}), 500
    
app.run(debug=True)

    







