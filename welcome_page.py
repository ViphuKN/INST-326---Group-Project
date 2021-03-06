import tkinter as tk
import requests
import json

"""Welcome page of the dog app"""

class Application(tk.Tk):
    """ To run the application of the GUI
    """
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x500')
        self.title('Welcome to the Find Dog Breed App')
        
        #Intro to the welcome page
        first_label = tk.Label(self, text = "Welcome", font=10) 
        #Pads for the Intro login screen
        first_label.pack(padx = 3, pady = 3) 

        #A button to login
        first_button = tk.Button(self, text ="Login", command = self.nextpage) 
        first_button.pack(padx= 5, pady = 5)
        #A button to register for an account
        second_button = tk.Button(self, text ="Register", command = self.sign_up) 
        second_button.pack(padx= 10, pady = 15)
        
    def nextpage(self):
        """ Go to the main menu page
        """
        tk.Tk.destroy(self) #This is to close the current page        
        import login_page

    def sign_up(self):
        """ Go to the sign up page
        """
        tk.Tk.destroy(self) #This is to close the current page        
        import sign_up_page

if __name__ == "__main__":
    app = Application()
    app.mainloop()