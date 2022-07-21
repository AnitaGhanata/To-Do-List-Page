import mysql.connector as conn

from flask import Flask, request, render_template, jsonify, json
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("login page.html" )
@app.route('/Welcomepage')
def Welcomepage():
     return render_template("welcom.html")   
@app.route('/PageCreateAccount')
def PageCreateAccount():
     return render_template("createaccount.html")
@app.route('/insert_login_data', methods=['POST', 'GET'])
def insert_login_data():
    result = ""
    if request.method == "POST":
        login_data = request.get_json()
        print(login_data)
        connection = conn.connect(host='localhost',port=3306,user='root',password='Gudgirls1@')
    try:
        cursor = connection.cursor()
        mySql_query = "INSERT INTO anitadb.Login (Email,Password) VALUES (%s, %s)"
        query = "SELECT * FROM anitadb.login"
        cursor.execute(query)
        login_database = cursor.fetchall()
        print(login_database)
        if not login_database:
            cursor.execute(mySql_query, login_data)
            connection.commit()
        else:
            for i in login_database:             
                if login_data[0]==i[1] and login_data[1]==i[2]:
                    print("email and password matched")
                    result = "success"
                else:
                    print("failed to login")
                    result = "fail"
    except:
            print("Failed to insert into MySQL table")    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            return jsonify(result)

@app.route('/insert_user_data', methods=['POST', 'GET'])
def insert_user_data():
    if request.method == "POST":
        qtc_data = request.get_json()
    connection = conn.connect(host='localhost',port=3306,user='root',password='Gudgirls1@')
    try:
        cursor = connection.cursor()
        mySql_query = "INSERT INTO anitadb.SignUP (Name,Phone_no,Email,Password) VALUES (%s, %s, %s, %s)"
        values=qtc_data
        query = "SELECT * FROM anitadb.signup"
        cursor.execute(query)
        records = cursor.fetchall()
        if not records:
            cursor.execute(mySql_query, values)
            connection.commit()
        else:
            for i in records:
                print(values[2])
                print(i[3])
                if values[2]==i[3]:
                    print("email matched")
                else:
                    print("failed to login")
    except:
            print("Failed to insert into MySQL table")    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            results = {'processed': 'true'}
            print(results)
            return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)