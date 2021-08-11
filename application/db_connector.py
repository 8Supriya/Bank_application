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
    except Exception as e:
        print(e)
