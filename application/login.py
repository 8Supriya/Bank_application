from bank_operation import balance_amount, deposit_amount
from db_connector import get_user_details


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
                    print('Withdraw')
                    login_value=''
                elif login_value==3:
                    balance_amount(user_id)
                    login_value=''
                elif login_value==4:
                    print('Statement')
                    login_value=''
                elif login_value==5:      
                    print('logout')
            except:
                print('\n\ninvalid input')        
            
    except Exception as e:
        print(e)
