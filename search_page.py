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
        first_label = tk.Label(self, text = "Search Info For Dogs", font=10)  #Try to have search for size, temperament, and breed
        #Pads for the Intro login screen
        first_label.pack(padx = 3, pady = 3) 

        #Weight for the dogs
        second_label = tk.Label(self, text = "Weight", font=10)  #Try to have search for size, temperament, and breed
        second_label.pack(padx = 3, pady = 3) 
        #Drop down Selections
        # weight_selections = OptionMenu(win, clicked, "Small", "Medium", "Large")
        
        #Breed type for the dogs
        third_label = tk.Label(self, text = "Breed Type", font=10)  #Try to have search for size, temperament, and breed
        third_label.pack(padx = 3, pady = 3) 
        #Drop down Selections
        # breed_selections = OptionMenu(win, clicked, "Small", "Medium", "Large")
        
        #Life span of the dogs
        fourth_label = tk.Label(self, text = "Lifespan", font=10)  #Try to have search for size, temperament, and breed
        fourth_label.pack(padx = 3, pady = 3) 
        #Drop down Selections
        # lifespan_selections = OptionMenu(win, clicked, "Short", "Medium", "Long")
        
        #A button to go to the search page
        first_button = tk.Button(self, text ="Show Results", command = self.results) 
        first_button.pack(padx= 5, pady = 5)
        
        #A button to go to the logout page
        third_button = tk.Button(self, text ="Logout", command = self.logout) 
        third_button.pack(padx= 5, pady = 5)
    
    def results(self):
        """ Go to the main menu page
        """
        tk.Tk.destroy(self) #This is to close the current page
        import results_page
        
    def logout(self):
        """ Direct the user to the welcome page if the user want to logout
        """
        tk.Tk.destroy(self) #This is to close the current page
        import welcome_page
      
app = Application()
app.mainloop()