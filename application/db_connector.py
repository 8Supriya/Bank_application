from statement import Statement
import mysql.connector


"""
This Method is used to insert user details
---------
Parameter : user_id -> user details  to be checked
---------
Logic
---------
1. Form a insert query dynamically using the user details
2. Handle exceptions using try
3. Get the DB connection
4. Get the cursor
5. Insert the query using the cursor
6. commit DB connection
8. Print exception details if the try block throws the exception

"""               
def insert_user_details(user_detail):
    insert_query="INSERT INTO `user_details`( `username`,`password`,`email_id`,`phone_no`,`aadhar no`,`pan_no`)VALUES('{}','{}','{}','{}','{}','{}')".format(user_detail.username,user_detail.password,user_detail.email_id,user_detail.phone_no,user_detail.aadhar_no,user_detail.pan_no)

    try:
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="bankapplication") 
        cursor= mydb.cursor()
        cursor.execute(insert_query) 
        mydb.commit()
    except Exception as e:
        print(e)

"""
This Method is used to get user details
---------
Parameter : user_id -> username and password to be checked
---------
Return : statement_list -> returns the balance amount 
---------
Logic
---------
1. Form a select query dynamically using the username and password
2. Handle exceptions using try
3. Get the DB connection
4. Get the cursor
5. Execute the query using the cursor
6. Fetchone from cursor and assign to user id
7. Get user id in string(it will be tuple) 
7. retrun the st
8. Print exception details if the try block throws the exception

"""               


def get_user_details(username,password):
    select_query="select user_id from user_details where username='{}' and password='{}'".format(username,password)

    try:
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="bankapplication") 
        cursor= mydb.cursor()
        cursor.execute(select_query)
        user_id=cursor.fetchone()
        if user_id: 
            st = ''.join(map(str, user_id))
            print('login successfully!!')
            return st
        else:
            print('invalid username and password')
            return ''    
    except Exception as e:
        print(e)


"""
This Method is used to insert statement
---------
Parameter : user_id -> statement to be checked
---------
Logic
---------
1. Form a insert query dynamically using the statement
2. Handle exceptions using try
3. Get the DB connection
4. Get the cursor
5. Insert the query using the cursor
6. commit DB connection
8. Print exception details if the try block throws the exception

"""               
def insert_statement(statement):
    insert_query="INSERT INTO `bankapplication`.`statement` (`user_id`, `transaction_type`, `date`, `amount`, `balance_amount`) VALUES ({}, '{}', '{}', {}, {})".format(statement.user_id,statement.transaction_type,statement.date,statement.amount,statement.balance_amount)
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="bankapplication") 
        cursor= mydb.cursor()
        cursor.execute(insert_query) 
        mydb.commit()
    except Exception as e:
        print(e) 


"""
This Method is used to get balance amount
---------
Parameter : user_id -> user_id  to be checked
---------
Return : statement_list -> returns the balance amount 
---------
Logic
---------
1. Form a select query dynamically using the user_id
2. Handle exceptions using try
3. Get the DB connection
4. Get the cursor
5. Execute the query using the cursor
6. Fetchone from cursor and assign to balance amount
7. Get balance amount in string(it will be tuple) 
7. retrun the 0
8. Print exception details if the try block throws the exception

"""               

def get_balance_amount(user_id):
    select_query="SELECT  balance_amount FROM statement where user_id ={} order by id desc limit 1".format(user_id)

    try:
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="bankapplication") 
        cursor= mydb.cursor()
        cursor.execute(select_query)
        balance_amount=cursor.fetchone()
        if balance_amount: 
            st = ''.join(map(str, balance_amount))
            return int(st)
        else:
            return 0    
    except Exception as e:
        print(e)

"""
This Method is used to get statement
---------
Parameter : user_id -> user_id  to be checked
---------
Return : statement_list -> returns the statement in list form
---------
Logic
---------
1. Form a select query dynamically using the user_id
2. Handle exceptions using try
3. Get the DB connection
4. Get the cursor
5. Execute the query using the cursor
6. Fetchall from cursor and assign to statement_list
7. retrun the statement_list
8. Print exception details if the try block throws the exception

"""


def get_statement(user_id):
    select_query="SELECT * FROM statement where user_id={}".format(user_id)

    try:
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="bankapplication") 
        cursor= mydb.cursor()
        cursor.execute(select_query)
        statement_list=cursor.fetchall()
        return statement_list
        
    except Exception as e:
        print(e)        

"""
This Method is used to check if the username is already exist
---------
Parameter : name -> username to be checked
---------
Return : user_data -> returns the user details if the username is already exist
---------
Logic
---------
1. Form a select query dynamically using the username
2. Handle exceptions using try
3. Get the DB connection
4. Get the cursor
5. Execute the query using the cursor
6. retrun the user data
7. Print exception details if the try block throws the exception
"""
def if_username_exist(name):
    select_query="SELECT * FROM user_details where username='{}'".format(name)

    try:
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="bankapplication") 
        cursor= mydb.cursor()
        cursor.execute(select_query)
        user_data=cursor.fetchone()
        return user_data
        
    except Exception as e:
        print(e)        
