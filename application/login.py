from bank_operation import amount_statement, balance_amount, deposit_amount, withdraw_amount
from db_connector import get_user_details


"""
This Function is used to define logic function
---------
Parameter : user_id -> to be checked
---------
Logic
---------
1. Handle exceptions using try
2. read username and password
3. Get details of username and password from get_user_details
4. Read Deposit amount.withdraw amount,blance amount,amount statement and logout
5. Print exception details if the try block throws the exception

"""               


def login_func():
    try:
        user_id=''
        while user_id=='':
            username=input('enter username:')
            password=input('enter password:')
            user_id=get_user_details(username,password)
    
        login_data='=============================================\nenter your choice:\n1. Deposit \n2. Withdraw \n3. Balance \n4. Statement \n5. Logout \n============================================= \n'
        login_value=''
        while login_value!=1 and login_value!=2 and login_value!=3 and login_value!=4 and login_value!=5:
            result=input(login_data)
            try:
                login_value=int(result)
                if login_value==1:
                    deposit_amount(user_id)
                    login_value=''
                elif login_value==2:
                    withdraw_amount(user_id)
                    login_value=''
                elif login_value==3:
                    balance_amount(user_id)
                    login_value=''
                elif login_value==4:
                    amount_statement(user_id)
                    login_value=''
                elif login_value==5:      
                    print('logout')
            except:
                print('\n\ninvalid input')        
            
    except Exception as e:
        print(e)
