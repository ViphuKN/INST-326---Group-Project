import tkinter as tk
import requests
import json

"""Search for the dog breed"""

class Application(tk.Tk):
    """ To run the application of the GUI
    """
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x500')
        self.title('Search Page')
        
        #Intro Menu Screen
        first_label = tk.Label(self, text = "INSERT TEXT HERE", font=10)  #Try to have search for size, temperament, and breed
        #Pads for the Intro login screen
        first_label.pack(padx = 3, pady = 3) 

        #A button to go to the search page
        first_button = tk.Button(self, text ="Show Results", command = self.results) 
        first_button.pack(padx= 5, pady = 5)
        
        #A button to go to the logout page
        second_button = tk.Button(self, text ="Favorites", command = self.favorite) 
        second_button.pack(padx= 5, pady = 5)
        
        #A button to go to the logout page
        third_button = tk.Button(self, text ="Logout", command = self.logout) 
        third_button.pack(padx= 5, pady = 5)
    
    def results(self):
        """ Go to the main menu page
        """
        tk.Tk.destroy(self) #This is to close the current page
        import results_page

    def favorite(self):
        """ Go to the favorite page
        """
        tk.Tk.destroy(self) #This is to close the current page
        import favorite_page
        
    def logout(self):
        """ Direct the user to the welcome page if the user want to logout
        """
        tk.Tk.destroy(self) #This is to close the current page
        import welcome_page
      
app = Application()
app.mainloop()