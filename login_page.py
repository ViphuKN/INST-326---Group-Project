import tkinter as tk
import requests
import json

"""Login page of the dog app"""

class Application(tk.Tk):
    """ To run the application of the GUI
    """
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x500')
        self.title('Login to Dog Breed App')
        
        #Intro login screen
        first_label = tk.Label(self, text = "Login Screen", font=10) 
        #Pads for the Intro login screen
        first_label.pack(padx = 3, pady = 3) 
        
        #Username label
        second_label = tk.Label(self, text = "Username:", font=10) 
        second_label.pack(padx = 3, pady = 3) 
        #First input 
        Application.first_entry = tk.Entry(self, width = 30) 
        Application.first_entry.pack(padx = 7, pady = 7)
        
        #Password label
        third_label = tk.Label(self, text = "Password:", font=10) 
        third_label.pack(padx = 3, pady = 3) 
        #Second input
        Application.second_entry = tk.Entry(self, width = 30) 
        Application.second_entry.pack(padx = 7, pady = 7)
        
        #A button to click after login info is completed
        first_button = tk.Button(self, text ="Login", command = self.main_menu) 
        first_button.pack(padx= 5, pady = 5)
        #A button to register for an account
        second_button = tk.Button(self, text ="Register", command = self.sign_up) 
        second_button.pack(padx= 10, pady = 15)
        
    def intro(self):
        """ To display the entries of the username and password
        """
        x = Application.first_entry.get()
        y = Application.second_entry.get()
        print(x, y)

    def main_menu(self):
        """ Go to the main menu page
        """
        tk.Tk.destroy(self) #This is to close the current page        
        import main_menu_page

    def sign_up(self):
        """ Go to the sign up page
        """
        tk.Tk.destroy(self) #This is to close the current page        
        import sign_up_page


app2 = Application()
app2.mainloop()