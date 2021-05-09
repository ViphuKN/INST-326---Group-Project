import tkinter as tk
import requests
import json

"""Main Menu of the app"""

class Application(tk.Tk):
    """ To run the application of the GUI
    """
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x500')
        self.title('Main Menu')
        
        #Intro Menu Screen
        first_label = tk.Label(self, text = "Choose a selection of the Dog Breed App", font=10) 
        #Pads for the Intro login screen
        first_label.pack(padx = 3, pady = 3) 

        #A button to go to the search page
        first_button = tk.Button(self, text ="Search", command = search) 
        first_button.pack(padx= 5, pady = 5)
        #A button to go to the favorite page
        second_button = tk.Button(self, text ="Favorite", command = favorite) 
        second_button.pack(padx= 5, pady = 5)
        #A button to go to the logout page
        third_button = tk.Button(self, text ="Logout", command = logout) 
        third_button.pack(padx= 5, pady = 5)
        
def favorite():
    """ Go to the favorite page
    """
    import favorite_page
    
def search():
    """ Go to the search page to select a dog breed
    """
    import search_page

def logout():
    """ Direct the user to the welcome page if the user want to logout
    """
    import welcome_page
    
if __name__ == "__main__":
    app = Application()
    app.mainloop()