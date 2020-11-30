import main
import Book_Ticket
import sqlite3
import re
import users_data
names=['Name']
name_s={}
air_database=sqlite3.connect('airline.db')
air_cursor=air_database.cursor()
class authen:
    def __init__(self,choice):
        print(50*"*")
        print("WELCOME TO TESLA'S AIRLINE RESERVATION")
        print(50*"*")
        #Check valid mobile and email address (2ND CALL)
        def pattern_Match():
            pattern_email=re.compile(r'[a-zA-Z0-9._+-]+@\w+\.\w+')
            pattern_mobile=re.compile(r'^[9876]\d{9}') 
            
            if(pattern_email.match(self.email)):
                if(choice=='C'):
                     if(pattern_mobile.match(self.mobile)):
                         return True
                else:
                    return True
            else:
                return False

        #Retry when error occured (1st EXECUTED)   
        while(1):
             self.email=input("Enter your Email: ")
             print(50*"*")
             if(choice=='C'):
                 self.name=input("Enter your Name: ")
                 print(50*"*")
                 self.mobile=(input("Enter your Mobile no: +91"))
                 print(50*"*")
             self.password=input("Enter your Password: ")
             print(50*"*")
             if(pattern_Match()):
                  break
             else:
                  print("Enter the correct credentials.....Try Again")
                  print(50*"*")
                  continue

                

    #CHECK LOGIN CRETENTIALS
    def Login(self):
             if(self.checkUser()):
                 main.home()
             else:
                 return
             return

    #USER CHECKING WITH THE SQLITE DATABASE
    def checkUser(self):
        check_query="SELECT Email from User_details where Email=='{}';".format(self.email)
        air_cursor.execute(check_query)
        get_result=air_cursor.fetchone()
        name_s=dict(zip(names,get_result))
        print(name_s)
        if(get_result==None or get_result[0]!=self.email):
            print("Invalid Account...Please Create an Account before Login")
            print(50*"*")
            return False
        else:
            return True

        
    #INVOKE THE DATABASE(CREATION)
    def CreateAc(self):
           self.create_user()
           main.home()
           return


    #UPLOAD THE USER DATA TO DATABASE(CREATION)
    def create_user(self):
        air_cursor.execute('''INSERT INTO User_details(Name,Email,Password,Phone_no)values(?,?,?,?);''',(self.name,self.email,self.password,self.mobile))
        air_database.commit()
     
get_choice=int(input("1.Login\n2.Create An Account\n"))
if(get_choice==1):
    s=authen('L')
    s.Login()
else:
    s=authen('C')
    s.CreateAc()
