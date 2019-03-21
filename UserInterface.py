#group number 18
import os
from tkinter import *
from Globals import *
master = Tk()

Label(master, text='Base Url').grid(row=0)
Label(master, text='Filters').grid(row=1)

e1 = Entry(master) 
e2 = Entry(master)

e1.grid(row=0, column=1) 
e2.grid(row=1, column=1)




def startCrawl():        
    base_url=(e1.get())
    filters=(e2.get())
    if(base_url!=None):
        
        file = open('testfile.txt','w') 
        file.write(base_url + ";" + filters)  
        file.close()
        
        os.system('main.py')        
    
           
        


    


Button(master,text="StartCrawl",font=('times new roman',20),bg="maroon",fg="white",command=startCrawl).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
mainloop()









