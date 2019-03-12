
from book import Book

class LinkedList:
    
    def __init__(self):#create an empty linked list
        self.head = None
        self.size = 0 #the list starts of with no books 
        
    def get_size(self):
        return self.size #return the size of the linked list
    
    def is_empty(self):
        return self.size == 0 #check if the linkedlist is empty
    

    def add_book_to_front(self, new_book):
        new_book.set_next_node(self.head)#the new book refers to the old first book(node)
        self.head = new_book #the head of the new book becomes the head of the list 
        self.size+=1 #the size of the list increases 
        
    def display_book(self):
        current = self.head #current book is at the head of the linked list when size is equal to zero
        while current != None: #current is equal to head print the book title, author, ibsn, publisher, and year of publicaiton. 
            print(current.get_title(), current.get_author(), current.get_ibsn(), current.get_publisher(), current.get_year_published())
            current = current.get_next_node()#current is the next book(node)
            
    def remove_book_location(self,value):
        prev = None 
        curr = self.head
        while curr:
            if curr.book_location == value:#curren is equal to a location
                if prev: 
                    prev.set_next_node(curr.get_next_node())#set previous equal to the current next book(node) and current is not the head of the list 
                else:
                    self.head = curr.get_next_node()#the nead is current next node
                return True
                    
            prev = curr# previous is equal to current
            curr = curr.get_next_node()#current becomes the next node 
            
        return False
              
    def sort_author_name(self):
        for i in range(1,self.size):
            node1 = self.head #book 1(node 1) is equal to the head 
            node2 = node1.get_next_node() #Book 2(node 2) is equal to the next node 
            while node2 is not None:
                if node1.author > node2.author:# author 1 is before author 2 alphabetically 
                    temp = node1.ibsn #node 1 value is stored in temp
                    temp2 = node1.title
                    temp3 = node1.author

                    node1.ibsn = node2.ibsn #node 1 ibsn, title, and author stores node 2 ibsn, title, and author
                    node1.title = node2.title
                    node1.author = node2.author

                    node2.ibsn = temp# mode 2 stores the values in temp. It taes up node 1 values 
                    node2.title = temp2
                    node2.author = temp3
                node1 = node1.get_next_node()# node 1 is set to the next node
                node2 = node2.get_next_node()#node 2 is set to the nex Node     
#


"""myLinkedList.add_book_to_front(nodeA)
myLinkedList.add_book_to_front(nodeB)
myLinkedList.add_book_to_front(nodeC)

myLinkedList.add_book_location(nodeD,1)
# myLinkedList.add_book_location(nodeE,1)
# myLinkedList.add_book_location(nodeF,1)


myLinkedList.remove_book_location(2)
# myLinkedList.remove_book_location(2)

myLinkedList.SortByAuthorName()
print(myLinkedList.get_size())
myLinkedList.display_book() """