import datetime
from book import Book
from datetime import date, timedelta

class Member:
    
    def __init__(self, name, age, address, library_card_number, borrowed_books={}):#create an empty member object
        self.name = name
        self.age = age
        self.address = address
        self.library_card_number = library_card_number
        self.borrowed_books = borrowed_books #{"IBSN22":20-12-2018,"IBSN99":12-1-2019}
        
    def get_name(self):
        return self.name # returns the number of the member
        
    def get_age(self):
        return self.age #returns the age of the member
        
    def get_address(sef):
        return self.address #returns the address of the member
        
    def get_card(self):
        return self.library_card_number #returns the library card number 
        
    def check_book_status(self, book):#checks the book status
        return book.is_available
        
    def borrow_book(self, book):
        if self.check_book_status(book):
            self.borrowed_books[book.ibsn] = self.get_due_date()#When a book is borrowed it is stored in a dictionary. The key is the ibsn and due date is the value.
        else:
            print("The book is not available")
          
    def get_renewal_date(self,book):
        get_input = input("Do you want to renew the book? y/n")#asks the user for an input
        if get_input == 'y':
            extend_tdelt = datetime.timedelta(days=14)#if user wants to renew the book after the due date the user must nenew the book for an additonal 14 days.
            self.borrowed_books[book.ibsn] = self.get_due_date()#calcuates the due date in a dictionary with ibsn key and due data value pair.
        elif get_input == 'n':#if no the book is returned
            print("Thank you for using our library")
        else:
            print("Please enter y or n")
	    
    def get_due_date(self):
        due_date = date.today() + timedelta(days=14)# 14 days is added
        print(due_date)#the due date is prnted 
        return due_date #When a book is borrowed, the book must be returned or renewed within 14 days. 
       

        
        #def find_balance(self):
        
        #def make_payment(self):
        
        #def extend_renewal(self):