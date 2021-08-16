from db_connector import if_username_exist, insert_user_details
from user_details import UserDetails
import re


def create_account():

    flag=False
    while flag==False:
        username=input('enter username : ')
        flag=validate_username(username)

    
    flag=False
    while flag==False:
        password=input('enter password : ')
        flag=validate_password(password)
    
    flag=False
    while flag==False:
        email_id=input('enter email id: ')
        flag=validate_email_id(email_id)
    
    flag=False
    while flag==False:
      phone_no=input('enter phone number : ')
      flag=validate_phone_no(phone_no)

    flag=False
    while flag==False:
     aadhar_no=input('enter aadhar no : ')
     flag=validate_aadhar_no(aadhar_no)
    
    flag=False
    while flag==False:
     pan_no=input('enter pan number : ')
     flag=validate_pan_no(pan_no)
    
    print('===========================================================')    
    print('please confirm the details')
    print('username is {}'.format(username))
    print('password is {}'.format(password))
    print('email_id is {}'.format(email_id))
    print('phone no is {}'.format(phone_no))
    print('aadhar no is {}'.format(aadhar_no))
    print('pan no is {}'.format(pan_no))
    print('=============================================================')

    result='========================================\nenter your choice:\n1. confirmation \n2. edit \n============================================= \n'
    num_value=''
    while num_value!=1 and num_value!=2:
        result2=input(result)
        try:
         num_value=int(result2)
         if num_value==1:
          user_detail= UserDetails(username,password,email_id,phone_no,aadhar_no,pan_no)
          insert_user_details(user_detail)
          print('successfully created')
          
         elif num_value==2:
          print('edit your details')
          create_account()
        except:
         print('\n\ninvalid input')        

    
    
    
# 1.This method is used to validate username 
# 2.Username should contain only alphabets
# 3.Username lenght should be >4 and <=10
# 4.Return true if username is valid or return false
def validate_username(name):
    if name.isalpha():
        if len(name) > 3 and len(name) <=10:
         data= if_username_exist(name)
         if data:
           print('username already exist')
           return False
         else:
             return True
        else:
          print('username should be more than 3 and less than 10 letters') 
          return False   
    else:
     print("name should contain only letters")
     return False  


# 1.This method is used to validate password 
# 2.Password should contain only alphanumeric
# 3.Password lenght should be >4 and <=10
# 4.Return true if Password is valid or return false
def validate_password(password):

    if password.isalnum() and not password.isalpha() and not password.isnumeric():
        if len(password) > 3 and len(password) <=10:
             return True
        else:
          print('passsword should be more than 3 and less than 10 letters') 
          return False   
    else:
     print("password should contain only alphanumeric")
     return False  


# 1.This method is used to validate email id
# 2.Password should contain only alphanumeric
# 3.Password lenght should be >4 and <=10
# 4.Return true if Password is valid or return false
    
def validate_email_id(email_id):
  regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
  if(re.fullmatch(regex, email_id)):
        return True
 
  else:
        print("Invalid Email")

# 1.This method is used to validate phone no
def validate_phone_no(phone_no):

    if phone_no.isnumeric():
        if len(phone_no)==10:
             return True
        else:
          print('phone no should be equal to 10 numbers') 
          return False   
    else:
     print("phone_no should contain only numeric")
     return False  

# 1.This method is used to validate aadhar number
def validate_aadhar_no(aadhar_no):

    if aadhar_no.isnumeric():
        if len(aadhar_no)==12:
             return True
        else:
          print('aadhar no should be equal to 12 numbers') 
          return False   
    else:
     print("aadhar_no shold contain only numeric")
     return False  

# 1.This method is used to validate pan number
def validate_pan_no(pan_no):    
    Result=re.compile("[A-Za-z]{5}\d{4}[A-Za-z]{1}") 
    check= Result.match(pan_no) 
    if (check):  
       return True     
    else : 
      print ("Invalid PAN Number entered.")
      return False

