import string
import re 
from member import Member 

class User(Member):
    def __init__(self, username, password, name, age, address, library_card_number):#create an empty user object
        Member.__init__(self,name, age, address, library_card_number)#user inherited member class
        self.check_password(password)#every user object must check and confirm their password. 

        self.username = username
        self.password = password
        
    def enter_username(self, username):
        return self.username #returns a username
    
    def enter_password(self, password):
        return self.password #returns a password 
    
    #def get_login_status(self, login_status):
    #    return self.login_status
    
    #def login_date(self, login_date):
    #    return self.login_date
    
    def ask_user(self):        
        username = input("Enter your username...") #asks user to type a username 
        password = input("Enter your password...")# asks user to type a password
        if self.username != username or self.password != password:
        	return False #if username or password is not correct then the login fails
        else:
        	return True# if username and password are correct then login is successful.
       
      
    def check_password(self, password):#checks if passwords is valid.
        lower_case = self.calc_lower(password) # all the lowercase letters in an alphabet
        upper_case = self.calc_upper(password) # all the upper case letters in an alphabet
        special_char = self.calc_special_char(password) #all the special characters in an alphabet return true or false 
        num_digits = self.calc_digits(password) # the numbers from 0 to 9 
        if len(password) > 7 and lower_case >= 1 and upper_case >= 1 and special_char and num_digits >= 1:
            print("Passowrd is valid")# a valid password is more than 7  characters long and contains at leaset 1 or more lower case, upper case, special character, and digit.
        else:  
            if lower_case < 1:
                print("Password has no lowercase.") #Password is not valid if it does not contain any lowercase
            elif upper_case < 1: #Password is not valid if it does not contain any uppercase
                print("Password has no uppercase.")
            elif not special_char :#Password is not valid if it does not contain any special character
                print("Password has no special characters")
            elif num_digits < 1:
                print("Password has no digits")#Password is not valid if it does not contain any digits
            else:
                print("Password is invalid. Please try again!")#Password is not correct for more than one reason
            
     
    def calc_special_char(self, s):
    
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') #special character set and pass the argument into the compile method    
         
        if(regex.search(s) == None):#check if the string contains special characters.The string is passed in the search and method object.
            return False
        else:
            return True

    def calc_digits(self, s):
        numbers_list = [int(i) for i in s if i.isdigit()]#stores the digits in a number's list
        return len(numbers_list)#returns the size of the list.
    
    def calc_lower(self, s):
        lower = [i for i in s if i.islower()]#stores the lowercase letters in a lower list
        return len(lower)#returns the number of lowercasse in the lower list

    def calc_upper(self, s):
        upper = [i for i in s if i.isupper()]#storess the uppercase letters in a upper list 
        return len(upper)#returns the number of upper case letter in the upper list