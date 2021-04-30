import tkinter as tk
import requests
import json

class Application(tk.Tk):
    """ To run the application of the GUI
    """
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x500')
        self.title('Welcome to the Find Dog Breed App')
        
        first_label = tk.Label(self, text = "Login Screen", font=10) #Intro login screen
        first_label.pack(padx = 3, pady = 3) #Pads for the Intro login screen
        second_label = tk.Label(self, text = "Username:", font=10) #Username label
        second_label.pack(padx = 3, pady = 3) 
        Application.first_entry = tk.Entry(self, width = 30) #First input 
        Application.first_entry.pack(padx = 7, pady = 7)
        third_label = tk.Label(self, text = "Password:", font=10) #Password label
        third_label.pack(padx = 3, pady = 3) 
        Application.second_entry = tk.Entry(self, width = 30) #Second input
        Application.second_entry.pack(padx = 7, pady = 7)
        first_button = tk.Button(self, text ="Login", command = nextpage) #A button to click after login info is completed
        first_button.pack(padx= 5, pady = 5)
        
        
def intro():
    """ To display the entries of the username and password
    """
    x = Application.first_entry.get()
    y = Application.second_entry.get()
    print(x, y)

def nextpage():
    """ Go to the next page of the GUI
    """
    import page_2
    
if __name__ == "__main__":
    app = Application()
    app.mainloop()