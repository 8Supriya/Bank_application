from db_connector import get_balance_amount, insert_statement
from statement import Statement 
from datetime import date


def deposit_amount(user_id):
    try:
        flag=False
        while flag==False:
            amount=input("Enter depsoit amount:")
            flag=validate_deposit(amount)

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
    
def validate_deposit(amount):
    if amount.isnumeric():
        if int(amount)<=40000:
             return True
        else:
          print('Amount exceeded(Amount should be lessthan 40000)  ') 
          return False   
    else:
     print("Invalid amount")
     return False  

    
def validate_withdraw(withdraw):
    if withdraw.isnumeric():
        if withdraw<=40000:
             return True
        else:
          print('Amount exceeded(Amount should be lessthan 40000)  ') 
          return False   
    else:
     print("Invalid amount")
     return False  

def balance_amount(user_id):
    balance=get_balance_amount(user_id)
    print('Your Balance is {}'.format(balance))

def amount_statement():
    print('amount deposited')

def logout():
    print('logout')

