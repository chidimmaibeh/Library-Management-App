from member import Member

class Librarian(Member):
  
    def __init__(self, name, age, address, library_card_number, phone, email):# create an empty librarian class
        Member.__init__(self,name, age, address, library_card_number)#inherits the member class 
        self.phone = phone
        self.email = email
        
    def get_name(self, member):
        member_name = member.get_name()# name is inherited from the member class
        return member # returns the librarian's name
    
    def get_age(self, age):
        member_age = member.get_age()#age is inherited from the member class
        return age# returns the librarian's age
    
    def get_address(self, address):
        member_address = member.get_address()#address is inherited from the address class
        return address#returns the librarian's address
    
    def add_new_book(self, new_book, my_linked_list):
        my_linked_list.add_book_to_front(new_book)#book added to front of linked list
    
    #def order_book():
        
    
    #def replace_book():
        
    
    #def get_library_balance():
        
    
    #def schedule_event():
        
    
    #def access_user_account():
        
    
    #def charge_fine():
        
 
 