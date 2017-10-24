from flask import Flask
from flask import render_template
from flask_mysqldb import MySQL
 
mysql = MySQL()
app = Flask(__name__)
# My SQL Instance configurations
# Change the HOST IP and Password to match your instance configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1001996'
app.config['MYSQL_DB'] = 'todolist'
app.config['MYSQL_HOST'] = '35.187.171.77'
mysql.init_app(app)

@app.route('/')
@app.route('/<name>')
def statichtml(name=None):
    return render_template('index.html', name=name)

@app.route("/list")
def hello(): # Name of the method
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''SELECT * FROM TASK''') # execute an SQL statment
    rv = cur.fetchall() #Retreive all rows returend by the SQL statment
    return render_template('index.html', name=str(rv))     #Return the data in a string format

@app.route("/add/<string:task>")
def add(task=None):
    cur= mysql.connection.cursor()
    cur.execute('''INSERT INTO TASK (task_name) VALUES (%s)''',(task,))
    mysql.connection.commit()
    return render_template('index.html', name="New Record is added to the database")


@app.route("/update/<task>/<no>")
def update(task=None, no=None):
    cur=mysql.connection.cursor()
    update_stmt = (
        "UPDATE TASK SET task_name = %s "
        "WHERE task_no = %s")
    data=(task,no)
    cur.execute(update_stmt, data)
    mysql.connection.commit()

    return render_template('index.html', name="User recored was updated")      #Return the data in a string format



@app.route("/delete/<no>")
def delete(no=None):
    cur=mysql.connection.cursor()
    delstatmt = "DELETE FROM TASK WHERE task_no = ' {} ' ".format(no)
    print(delstatmt)

    cur.execute(delstatmt)
    mysql.connection.commit()
    return render_template('index.html', name="User recored was deleted")      #Return the data in a string format
if __name__ == "__main__":
        app.run(host='0.0.0.0', port='5000')
