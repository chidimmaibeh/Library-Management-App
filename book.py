

class Book:

    def __init__(self, title, author, ibsn, publisher, year_published, book_location, is_available=True, nextNode=None):#create an empty book object
        self.title = title
        self.author = author
        self.ibsn = ibsn
        self.publisher = publisher
        self.year_published = year_published
        self.book_location = book_location
        self.is_available = is_available #checks if book is in the library or not 
        self.next_node = nextNode


    def get_title(self):
        return self.title #returns a book's title

    def get_author(self):
        return self.author# returns a book's author

    def get_ibsn(self):
        return self.ibsn #returns a book's ibsn

    def get_publisher(self):
        return self.publisher #returns a book's publisher

    def get_year_published(self):
        return self.year_published #returns a book's year of publication
        
    def find_book_location(self):
        return self.book_location #returns a book location

    def get_next_node(self):
        return self.next_node #returns and finds the book after the curreent book (node) as the next node 

    def set_next_node(self,new_book):
        self.next_node = new_book #set the book after the current book (node) as the next node


        #def read_description():
            
        
        #def view_sample():
        
        
       # def write_review():