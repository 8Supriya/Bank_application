import mysql.connector

def insert_user_details(user_detail):
    insert_query="INSERT INTO `user_details`( `username`,`password`,`email_id`,`phone_no`,`aadhar no`,`pan_no`)VALUES('{}','{}','{}','{}','{}','{}')".format(user_detail.username,user_detail.password,user_detail.email_id,user_detail.phone_no,user_detail.aadhar_no,user_detail.pan_no)

    try:
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="bankapplication") 
        cursor= mydb.cursor()
        cursor.execute(insert_query) 
        mydb.commit()
    except Exception as e:
        print(e)

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


def insert_statement(statement):
    insert_query="INSERT INTO `bankapplication`.`statement` (`user_id`, `transaction_type`, `date`, `amount`, `balance_amount`) VALUES ({}, '{}', '{}', {}, {})".format(statement.user_id,statement.transaction_type,statement.date,statement.amount,statement.balance_amount)
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="bankapplication") 
        cursor= mydb.cursor()
        cursor.execute(insert_query) 
        mydb.commit()
    except Exception as e:
        print(e)        

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