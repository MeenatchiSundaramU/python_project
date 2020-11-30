import sqlite3
bkt_connect=sqlite3.connect('airline.db')
bkt_cursor=bkt_connect.cursor()
names=['Airplane Name','From','To','Total Seats','Total Price']
merge_dict={}
class Book_Ticket:
    def __init__(self):
        print(50*"*")
        print("Welcome to Ticket Booking Page\n")
        print(50*"*")
        self.froms=input("Enter the Depature Place\n")
        print(50*"*")
        self.tos=input("Enter the Arrival Place\n")
        print(50*"*")
        self.date=input("Enter the Date of Depature\n")
        print(50*"*")
        self.choice=int(input("Choose the economies 1.economy 2.premium economy 3.business 4.first class"))
        print(50*"*")
        if(self.choice==1):
            self.choice_total="economy_total"
            self.choice_price="eco_price"
        elif(self.choice==2):
            self.choice_total="premium_total"
            self.choice_price="premium_price"
        elif(self.choice==3):
            self.choice_total="business_total"
            self.choice_price="busi_price"
        else:
            self.choice_total="first_total"
            self.choice_price="first_price"

            
    def retrievalData(self):
        bkt_search="SELECT air_name,froms,tos,{},{} from Vehicle_Info where tos=='{}' and froms=='{}';".format(self.choice_total,self.choice_price,self.tos,self.froms)
        bkt_cursor.execute(bkt_search)
        result=bkt_cursor.fetchone()
        merge_dict=dict(zip(names,result))
        print(merge_dict)
        for i in names:
            print("{}  :  {}".format(i,merge_dict[i]))
            print(50*"*")
        self.tpass=int(input("Enter the Total Passengers\n"))
        print(50*"*")
        get_bkt=input("Are you Sure you want to book the Ticket (yes/no\n")
        if(get_bkt=='yes'):
             self.update_data(self.tpass,merge_dict['Airplane Name'])
             print("Total Price :Rs.",merge_dict['Total Price']*self.tpass)
             print(50*"*")
        else:
            return
    
    def update_data(self,get_pass,plane_name):
        update_query="UPDATE Vehicle_Info SET {}={}-{} where tos=='{}' and froms=='{}' and air_name=='{}';".format(self.choice_total,self.choice_total,get_pass,self.tos,self.froms,plane_name)
        bkt_cursor.execute(update_query)
        bkt_connect.commit()
        print("Updated Successfully")
    
def tktBook():
    ibkt=Book_Ticket()
    ibkt.retrievalData()

