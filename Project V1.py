# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 09:13:47 2021

@author: Ayush Padhy
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
root=Tk()
root.title("Enter Details")
root.geometry("1000x600")

 


import datetime
import calendar
 
def findDay(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[born])

 

def Submit():
    global From
    From=fromenter.get()
    global to
    To=toenter.get()
    global Date
    Date= str(dd.get()) + " " + str((Months.index(mm.get()))+1) + " "+ str(yy.get())
    global day
    day=findDay(Date)
    
    print("The Boarding Location is : " + From)
    print("The Final Destination is : " + To)
    print("The Date of Travel is : " + Date)  
    print("The Day of Travel is : " + day)
    

    
    
    
from_=Label(root, text="From: ", font="50")
from_.grid(row= 0, column= 0, sticky= W, pady=2)
n = StringVar()
fromenter= ttk.Combobox(root, width = 70, textvariable = n)
fromenter['values'] = ('Ahmedabad','New Delhi', 'Mumbai', 'Vadodara', 'Bangaluru', 'Hyderabad', 'Bhubaneswar',
                       'Chennai','Kolkata')
fromenter.grid(row= 0, column= 1)


to_=Label(root, text="To: ", font="50")
to_.grid(row= 1, column= 0, sticky= W, pady=2)
n = StringVar()
toenter= ttk.Combobox(root, width = 70, textvariable = n)
toenter['values'] = ('Ahmedabad','New Delhi', 'Mumbai', 'Vadodara', 'Bangaluru', 'Hyderabad', 'Bhubaneswar',
                        'Chennai','Kolkata')
toenter.grid(row= 1, column= 1)

 


Date_=Label(root, text="Date of Journey: ", font="50")
Date_.grid(row= 2, column= 0, sticky= W, pady=2)
dd=Spinbox(root, from_= 0, to = 31, width=5) 
dd.grid(row=2, column=1, sticky=W)
n = StringVar() 

 


#I know we discussed for Day instead of date but I have an idea, execute karne
#ka time nahi mila, baad main batata hoon

 

mm=ttk.Combobox(root, width = 27, textvariable = n)
Months=[' January',  
                          ' February', 
                          ' March', 
                          ' April', 
                          ' May', 
                          ' June', 
                          ' July', 
                          ' August', 
                          ' September', 
                          ' October', 
                          ' November', 
                          ' December']
mm['values'] = (' January',  
                          ' February', 
                          ' March', 
                          ' April', 
                          ' May', 
                          ' June', 
                          ' July', 
                          ' August', 
                          ' September', 
                          ' October', 
                          ' November', 
                          ' December') 

 

mm.grid(column = 1, row = 2, ) 

 

yy=Spinbox(root, from_= 2021, to = 2023, width=10) 
yy.grid(row=2, column=1, sticky=E)

 

submit=Button(root, text="Submit", bd='5', command=Submit)
submit.grid(row=3,column=1)



root.mainloop()