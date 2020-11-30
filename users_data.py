import sqlite3
users_list=['Name','Email','Phone_no']
user_data={}
bkt_connect=sqlite3.connect('airline.db')
bkt_cursor=bkt_connect.cursor()


def login_user():
     user_query="SELECT Name,Email,Phone_no from User_details where name=='Mano';"
     bkt_cursor.execute(user_query)
     result=bkt_cursor.fetchone()
     user_data=dict(zip(users_list,result))
