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
        first_label = tk.Label(self, text = "~Dog Info Results~", font=10)  #Display the results of what dogs the user can get
        #Pads for the Intro login screen
        first_label.pack(padx = 3, pady = 3) 
        
        #Display the info for breeds
        second_label = tk.Label(self, text = "Dog Breed:")
        second_label.pack(padx = 3, pady = 3) 
        
        #Button to reveal the output
        button = tk.Button(self, text="Reveal", command = self.dog_breed) 
        button.pack()
        
        #Display the info for the temperaments
        third_label = tk.Label(self, text = "Dog temperament:")
        third_label.pack(padx = 3, pady = 3) 

        #Button to reveal the output
        button_2 = tk.Button(self, text="Reveal", command = self.dog_temperament) 
        button_2.pack()        
        
        #Display the info for the heights
        fourth_label = tk.Label(self, text = "Dog height:")
        fourth_label.pack(padx = 3, pady = 3) 

        #Button to reveal the output
        button_3 = tk.Button(self, text="Reveal", command = self.dog_height) 
        button_3.pack()
        
        #Display the info for the weight (size)
        fifth_label = tk.Label(self, text = "Dog weight (size):")
        fifth_label.pack(padx = 3, pady = 3) 

        #Button to reveal the output
        button_4 = tk.Button(self, text="Reveal", command = self.dog_weight) 
        button_4.pack()

        #Display the info for the lifespan
        sixth_label = tk.Label(self, text = "Dog lifespan:")
        sixth_label.pack(padx = 3, pady = 3) 

        #Button to reveal the output
        button_5 = tk.Button(self, text="Reveal", command = self.dog_lifespan) 
        button_5.pack()    
    
        #A button to go to the search page
        first_button = tk.Button(self, text ="Search", command = self.search) 
        first_button.pack(padx= 5, pady = 5)

        #A button to go to the logout page
        third_button = tk.Button(self, text ="Logout", command = self.logout) 
        third_button.pack(padx= 5, pady = 5)
        
    def dog_breed(self):
        """Dog Breed Results
        """
        label = tk.Label(self, text= "Dog Breed")    
        label.pack(padx = 3, pady = 3) 
        
    def dog_temperament(self):
        """Dog temperament result
        """ 
        label = tk.Label(self, text= "Dog temperament")    
        label.pack(padx = 3, pady = 3) 
        
    def dog_height(self):
        """Dog height result
        """ 
        label = tk.Label(self, text= "Dog height")    
        label.pack(padx = 3, pady = 3) 

    def dog_weight(self):
        """Dog weight result
        """ 
        label = tk.Label(self, text= "Dog weight")    
        label.pack(padx = 3, pady = 3) 
        
    def dog_lifespan(self):
        """Dog lifespan result
        """ 
        label = tk.Label(self, text= "Dog lifespan")    
        label.pack(padx = 3, pady = 3) 
        
    def search(self):
        """ Go to the search page to select a dog breed
        """
        tk.Tk.destroy(self) #This is to close the current page
        import search_page

    def logout(self):
        """ Direct the user to the welcome page if the user want to logout
        """
        tk.Tk.destroy(self) #This is to close the current page
        import welcome_page
    
      
app = Application()
app.mainloop()