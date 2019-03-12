from user import User
from member import Member
from librarian import Librarian
from book import Book
from book_linked_list import LinkedList

class Library:
    
    def __init__(self, name, address, phone, email, days_of_week, hours):# creaet an empty Library 
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.days_of_week = days_of_week
        self.hours = hours
    
    def get_name(self, name):
        return self.name# return the name of the library
    
    def find_library_location(self, address):
        return self.address #return the locaton of the library
    
    def get_phone(self, phone):
        return self.phone # returns the library phone number 
    
    def get_email(self, email):
        return self.email# return the library email 
    
    def get_days(self, days):
        return self.days_of_week #returns the days opened 
    
    def check_library_hours(self, hours):
        return self.hours # returns the library hours of operation

def main():
                    

    create_library = Library("Appleton", "234 Lindenwoon Place", "614-358-3224", "info@appletonlib.com", "Mon to Fri", "8 to 5") #initalize the library object 
    print(create_library.name)# library name
    print(create_library.address)# library phone
    print(create_library.phone)# library phone
    print(create_library.email)# library email
    print(create_library.days_of_week)# library days of the week
    print(create_library.hours)#libaray hours
    myLinkedList = LinkedList()# initalize a linked list object

    librarian_one = Librarian('Ama Bates', '34', '90 Forestview Rd', '123456', '614-358-3223', 'abates@appletonlib.com')#created a library
    #the six book objects are created
    node_a = Book("Computer Science","Jenna Carlos","2401","New York Lib","2018", 1) #Book 1
    node_b = Book("Introduction to Chemistry","Jasmiine Futon","2402","New York Lib","2007", 2)#Book 2
    node_c = Book("General Biology","Maria Cantos","2403","New York Lib","2018", 3)#Book 
    node_d = Book("Material Engineering","David Leman","2404","New York Lib","2019", 4)# Book 4
    node_e = Book("Python Programming", "Melissa Bridges", "2405", "Midwest Publisher", 2002, 5)# Book 5 
    node_f = Book("Ecological Chemistry", "Anu Lu", "2406", "Midwest Publisher", 2010, 6)# Book 6


    myLinkedList.add_book_to_front(node_a)#six books are addded to the book linked list
    myLinkedList.add_book_to_front(node_b)
    myLinkedList.add_book_to_front(node_c)
    myLinkedList.add_book_to_front(node_d)
    myLinkedList.add_book_to_front(node_e)
    myLinkedList.add_book_to_front(node_f)#the head of the list
  

    user_one = User('Ama', 'Password6&', '90 Forestview Rd', '123456', '614-358-3223', 'abates@appletonlib.com')#the librarian has an user account
    # and checks to see if the password Password6& is valid.

    result = user_one.ask_user()# asks the user to confirm their username and password
    if result:
        user_one.borrow_book(node_d)#user borrows book(node D) and a due date is printed to the shell
    else:
        print("Wrong Username OR password")#prints to the shell if username and password is incorrect.



    myLinkedList.remove_book_location(node_a.book_location)#book(node a) is removed from the list
    myLinkedList.display_book()#the five books are printed to the shell(from node f to node b). Node f is in front/
    myLinkedList.sort_author_name()#the list is sorted by author last name
    print("The Sorted Linked List")
    myLinkedList.display_book()#the sorted linked list is printed to the shell. 


    
   

main()
    
        
    
    
    
        

