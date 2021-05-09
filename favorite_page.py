import tkinter as tk
import requests
import json

"""Display results from the search"""

class Application(tk.Tk):
    """ To run the application of the GUI
    """
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x500')
        self.title('Results')
        
        #Intro Menu Screen
        first_label = tk.Label(self, text = "INSERT TEXT HERE", font=10)  #Display the favorite dogs
        #Pads for the Intro login screen
        first_label.pack(padx = 3, pady = 3) 

        #A button to go to the search page
        first_button = tk.Button(self, text ="Search", command = search) 
        first_button.pack(padx= 5, pady = 5)
        
        
        #A button to go to the logout page
        second_button = tk.Button(self, text ="Logout", command = logout) 
        second_button.pack(padx= 5, pady = 5)
        
        
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