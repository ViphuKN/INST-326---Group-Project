import tkinter as tk
import requests
import json

"""Sign up to create an account"""

class Application(tk.Tk):
    """ To run the application of the GUI
    """
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x500')
        self.title('Register Account')
        
        #Intro login screen
        first_label = tk.Label(self, text = "Create an Account", font=10) 
        #Pads for the Intro login screen
        first_label.pack(padx = 3, pady = 3) 
        
        #Username label
        second_label = tk.Label(self, text = "Username:", font=10) 
        second_label.pack(padx = 3, pady = 3)
        #First input for username
        Application.first_entry = tk.Entry(self, width = 30) 
        Application.first_entry.pack(padx = 7, pady = 7) 
        #Confirmation Username label
        second_confirm_label = tk.Label(self, text = "Confirm Username:", font=10) 
        second_confirm_label.pack(padx = 3, pady = 3) 
        #Second input for confirm username
        Application.second_entry = tk.Entry(self, width = 30) 
        Application.second_entry.pack(padx = 7, pady = 7)
        
        #Password label
        third_label = tk.Label(self, text = "Password:", font=10) 
        third_label.pack(padx = 3, pady = 3) 
        #First input for password
        Application.third_entry = tk.Entry(self, width = 30) 
        Application.third_entry.pack(padx = 7, pady = 7)
        #Confirmation Password label
        fourth_confirm_label = tk.Label(self, text = "Confirm Password:", font=10) 
        fourth_confirm_label.pack(padx = 3, pady = 3) 
        #Second input for confirm password
        Application.fourth_entry = tk.Entry(self, width = 30) 
        Application.fourth_entry.pack(padx = 7, pady = 7)
        
        #A button to click after login info is completed
        first_button = tk.Button(self, text ="Login", command = main_menu) 
        first_button.pack(padx= 5, pady = 5)
        #A button to go back to the login page
        second_button = tk.Button(self, text ="Go Back", command = login) 
        second_button.pack(padx= 5, pady = 5)
        
def intro():
    """ To display the entries of the username and password
    """
    x = Application.first_entry.get()
    x1 = Application.second_entry.get()
    y = Application.third_entry.get()
    y1 = Application.fourth_entry.get()
    print(x, x1, y, y1)

def main_menu():
    """ Successful Login
    """
    import main_menu_page

def login():
    """ Go to the previous page
    """
    import login_page
    
if __name__ == "__main__":
    app = Application()
    app.mainloop()