'''TK Poll v3 By Andrew Ault
5/4/18
'''
from tkinter import *
from tkinter import messagebox
import ast
data = {}
try:
    file = open("file.txt","r")
    data = file.read()
    data = ast.literal_eval(data)
    file.close()
except:
    data = {}
root = Tk()
root.title("Tk Poll v3")

Label(root, text="Name").grid(row=0,column=0)
Label(root, text="How many pets").grid(row=1,column=0)

e1 = Entry(root)
e2 = Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

def sumbitInput():
    name = e1.get()
    number = e2.get()
    try:
        number = int(number)
    except:
        messagebox.showerror("Box Title","Not a Valid Number")
        return
    if name == "" or name in data:
        messagebox.showerror("Box Title","Not a Valid Name")
        return
    if number < 0:
        messagebox.showerror("Box Title","Cant be 0")
        return
    data[name] = number
    messagebox.showinfo("Title",data)
    e1.delete(0,END)
    e2.delete(0,END)
    file = open("file.txt","w")
    file.write( str(data) )
    file.close()
    
button = Button(root,text="Submit",command=sumbitInput)
button.grid(row=2,column=0)
def calcAverage():
    messagebox.showinfo("title",str(len(data))+" responses")
    if len(data) > 0:
        messagebox.showinfo("Average",sum(data.values())/ len(data))
button2 = Button(root,text="Average",command=calcAverage)
button2.grid(row=2,column=1)
button3 = Button(root,text="Quit",command=root.destroy)
button3.grid(row=2,column=2)
    
