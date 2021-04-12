""" Group Project: Making a Dog Breed App to allow users to find the right breed for them
    Group Names: Viphu Nguyen, Gerson Roldan, Peter Chen, Donna Arndt
"""

class Login():
    """ The features of having a login page
    """

def login_screen():
    """ Create login screen for the user to access the app
    
    Args:

    
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

def main():
    """ Main Function
    
    Args:
    """
    
if __name__ == "__main__":
    login_screen()