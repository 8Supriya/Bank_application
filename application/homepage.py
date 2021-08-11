from login import login_func
from create_account import create_account


heading='=============================================\nenter your choice:\n1. login \n2. create account \n3. exit \n============================================= \n'
int_value=''
while int_value!=1 and int_value!=2 and int_value!=3:
    result=input(heading)
    try:
        int_value=int(result)
        if int_value==1:
          login_func()
          int_value=''
        elif int_value==2:
          create_account()
          int_value=''
        elif int_value==3:
          print('exit')
    except:
        print('\n\ninvalid input')        
    
