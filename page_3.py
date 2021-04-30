from tkinter import *
import requests
import json

dogs_apik = '100ae381-76de-48ed-8a6d-73c6e11af170'
response = requests.get("https://api.thedogapi.com/v1/breeds")

class Application(Tk):
    """ To run the application of the GUI
    """
    def __init__(self):
        Tk.__init__(self)
        self.geometry('500x500')
        self.title('Welcome to the Find Dog Breed App')
        
        first_label = tk.Label(self, text = "Results of the Dog Breeds", font=10) #Intro login screen
        first_label.pack(padx = 3, pady = 3) #Pads for the Intro login screen
        count = 1
        for x in response.json():
            #print(count, "Dog's name: " + x["name"]) #Dog's name
            while count < 6: #Only display 5 dogs (for testing)
                print([count], x["name"] + "'s temperament: " + x["temperament"]) #Dog's temperament
                count += 1    
    
        first_button = tk.Button(self, text ="Button", command = nextpage) #A button to click after login info is completed
        first_button.pack(padx= 5, pady = 5)

ws = Tk()
ws.geometry('400x300')
ws.title('PythonGuides')
ws['bg']='#ffbf00'
f = ("Times bold", 14)

Label(
    ws,
    text="This is third page",
    padx=20,
    pady=20,
    bg='#ffbf00',
    font=f
).pack(expand=True, fill=BOTH)
 
def nextPage():
    """ Go to the next page
    """
    ws.destroy()
    import page_4

def prevPage():
    """ Go to the previous page
    """
    ws.destroy()
    import page_2

Button(
    ws, 
    text="Previous Page", 
    font=f,
    command=prevPage
    ).pack(fill=X, expand=TRUE, side=LEFT)
Button(
    ws, 
    text="Next Page", 
    font=f,
    command=nextPage
    ).pack(fill=X, expand=TRUE, side=LEFT)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
    ws.mainloop()
