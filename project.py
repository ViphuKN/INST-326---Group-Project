""" Group Project: Making a Dog Breed App to allow users to find the right breed for them
    Group Names: Viphu Nguyen, Gerson Roldan, Peter Chen, Donna Arndt
"""
import tkinter as tk


class Users():
    """list of users
    """
    def __init__(self, user_name):
        self.users = []


    def add_user(self, user_name):
        """adds user to list
        """
        self.users.append(user_name)
    
    def remove_user(self, user):
        """removes user from list
        """
        if self.users:
            self.users.remove(user)
        else:
            print("There are no users yet.")  

class User():
    """The features of having a user
    """
    def __init__(self, fname, lname):
        self.first = fname
        self.last = lname
        self.user_name = ""
        self.password = ""
        self.zip_code = 0

def login_screen():
    """ Create login screen for the user to access the app
    """
    print("*"*5, "Welcome to the Find Dog Breed App", "*"*5) #Print the intro of the login
    print("Enter 0 if you forgot your username/email address") #If the user forgot their username or email address login
    user_email = str(input("Username/Email address: " )) #User input the username or email address
    if user_email == "0":
        username()
    else:
        pass
    user_password = input("Password: ") #User input the password
    print("Successfully logged in!")

    
def username():
    """To allow the user to create their username or email address
    
    Args:
        username/email address: the name or email of the user created
    
    Return:
        user_email: the new username or email address given by the user
    """
    user_email = input("Enter your new username or email address: ")
    return user_email 

class Application(tk.Tk):
    """ The GUI of the app screen
    """
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x500')
        self.title('Your first App')
        first_label = tk.Label(self, text = "I'm a cool App!!", font=10)
        first_label.pack(pady= 2, padx = 2)


def main():
    """ Main Function
    
    Args:
    """
    
if __name__ == "__main__":
    
    app = Application()
    app.mainloop()