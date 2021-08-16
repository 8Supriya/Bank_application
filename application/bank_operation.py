from db_connector import get_balance_amount, get_statement, insert_statement
from statement import Statement 
from datetime import date


"""
This Function is used to define deposit amount
---------
Parameter : user_id -> to be checked
---------
Logic
---------
1. Handle exceptions using try
2. set flag to False
3. Read deposit amount and validate
4. Convert string amount into integer
5. Take balance amount from get_balance_amount function
6. Take statement from insert_statement function 
7. Print Deposited Successfully!!
8. Print exception details if the try block throws the exception

"""               

def deposit_amount(user_id):
    try:
        flag=False
        while flag==False:
            amount=input("Enter depsoit amount:")
            flag=validate_amount(amount)

        amount=int(amount)
        transaction_type='DEPOSIT'
        today = date.today()
        balance_amount=get_balance_amount(user_id)
        
        if balance_amount==0:
            balance_amount=amount
        else:
            balance_amount=balance_amount+amount    

        statement=Statement(user_id,transaction_type,today,amount,balance_amount) 
        insert_statement(statement) 
        print('Deposited Successfully!!')
    except Exception as e:
        print(e)


"""
This Function is used to validate amount
---------
Parameter : amount -> to be checked
---------
Logic
---------
1. validating amount
2. retrun true and false
"""               

def validate_amount(amount):
    if amount.isnumeric():
        if int(amount)<=40000:
             return True
        else:
          print('Amount exceeded(Amount should be lessthan 40000)  ') 
          return False   
    else:
     print("Invalid amount")
     return False  


"""
This Function is used to define withdraw amount
---------
Parameter : user_id -> to be checked
---------
Logic
---------
1. Handle exceptions using try
2. set flag to False
3. Read withdraw amount and validate
4. Convert string amount into integer
5. Take statement from insert_statement function 
6. Print Withdraw Successfully!!
7. Print exception details if the try block throws the exception

"""               

def withdraw_amount(user_id):
    try:
        flag=False
        while flag==False:
            amount=input("Enter withdraw amount:")
            flag=validate_amount(amount)

        amount=int(amount)
        transaction_type='WITHDRAW'
        today = date.today()
        balance_amount=get_balance_amount(user_id)
        
        if balance_amount<=amount:
            print('you dont have sufficient balance')
        else:
            balance_amount=balance_amount-amount    
            statement=Statement(user_id,transaction_type,today,amount,balance_amount) 
            insert_statement(statement) 
            print('Withdraw Successfully!!')
    except Exception as e:
        print(e)
    

"""
This Function is used to balance amount
---------
Parameter : user id -> to be checked
---------
Logic
---------
1. Get balance from get_balance_amount function
2. Print balance 
"""                   

def balance_amount(user_id):
    balance=get_balance_amount(user_id)
    print('Your Balance is {}'.format(balance))


"""
This Function is used to define amount statement
---------
Parameter : user_id -> to be checked
---------
Logic
---------
1. Handle exceptions using try
2. Take statement list from get_statement
3. Print exception details if the try block throws the exception

"""               

def amount_statement(user_id):
    try:
        statement_list=get_statement(user_id)
        print('======================================================================================')
        print('Your statement is as follows:')
        print('Date         ' ,'Amount          '  ,'Transaction_Type       '  ,'Balance')
        for row in statement_list:
            date=row[3]
            amount=row[4]
            transaction_type=row[2]
            balance=row[-1]
            print(f"{date}      {amount}                {transaction_type}              {balance}")
        print('=======================================================================================')
        
       
    except Exception as e:
        print(e)



def logout():
    print('logout')

