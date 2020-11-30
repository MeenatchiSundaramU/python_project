import Book_Ticket
class Home:
    def __init__(self):
        print("WELCOME TO HOME PAGE")
    def book_ticket(self):
        print("Book Ticket")
        Book_Ticket.tktBook()
        return
    def cancel_ticket(self):
        print("Cancel Ticket")
        return
    def flight_status(self):
        print("Flight Status")
        return


def home():
       h=Home()
       while(1):
           choice=int(input("1.BOOK TICKET\n2.CANCEL TICKET\n3.FLIGHT STATUS\n4.Exit\n"))
           if(choice==1):
               h.book_ticket()
           elif(choice==2):
                h.cancel_ticket()
           elif(choice==3):
                h.flight_status()
           else:
               break
