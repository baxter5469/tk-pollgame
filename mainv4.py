'''TK Poll v4 By Andrew Ault
5/4/18
'''
from tkinter import *
import ast
try:
    file = open("filev4.txt","r")
    data = file.read()
    data = ast.literal_eval(data)
    file.close()
except:
    data = {}
root = Tk()
root.title("Tk Poll v4")

Label(root, text="Enter your Name:").grid(row=0,column=0)
Label(root, text="How many pets:").grid(row=1,column=0)
Label(root, text="How many siblings:").grid(row=2,column=0)
Label(root, text="How many video games:").grid(row=3,column=0)
Label(root, text="How many movies:").grid(row=4,column=0)
Label(root, text="Enter your Age:").grid(row=5,column=0)
e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)
e5 = Entry(root)
e6 = Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)

def isValidNumber(checkme):
    try:
        pets = float(e2.get())
    except:
        messagebox.showerror("title" + checkme +" Is not a valid number")
    try:
        sibs = float(e3.get())
    except:
        messagebox.showerror("title" + checkme +" Is not a valid number")
    try:
        games = float(e4.get())
    except:
        messagebox.showerror("title" + checkme +" Is not a valid number")
    try:
        movies = float(e5.get())
    except:
        messagebox.showerror("title" + checkme +" Is not a valid number")
    try:
        age = float(e6.get())
    except:
        messagebox.showerror("title" + checkme +" Is not a valid number")
def sumbitInput():
    name = e1.get()
    if name == "" or name in data:
        messagebox.showerror("Box Title","Not a Valid Name")
        return
    pets = isValidNumber(e2.get())
    sibs = isValidNumber(e3.get())
    games = isValidNumber(e4.get())
    movies = isValidNumber(e5.get())
    age = isValidNumber(e6.get())
    data[name] = {}
    data[name]["age"] = age
    data[name]["sibs"] = sibs
    data[name]["games"] = games
    data[name]["movies"] = movies
    data[name]["pets"] = pets
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    file = open("filev4.txt","w")
    file.write( str(data) )
    file.close()
    
button = Button(root,text="Submit",command=sumbitInput)
button.grid(row=6,column=0)
def calcAverage():
    messagebox.showinfo("title",str(len(data))+" responses")
    if len(data) > 0:
        totalage = 0
        totalsibs = 0
        totalgames = 0
        totalmovies = 0
        totalpets = 0
        for name in data:
            totalage += data[name]["age"]
            totalsibs += data[name]["sibs"]
            totalgames += data[name]["games"]
            totalmovies += data[name]["movies"]
            totalpets += data[name]["pets"]
        messagebox.showinfo("Age Avg",str(totalage/len(data))+"is the average age")
        messagebox.showinfo("Sibs Avg",str(totalsibs/len(data))+"is the average siblings")
        messagebox.showinfo("Games Avg",str(totalgames/len(data))+"is the average games")
        messagebox.showinfo("Movies Avg",str(totalmovies/len(data))+"is the average movies")
        messagebox.showinfo("Pets Avg",str(totalpets/len(data))+"is the average pets")
button2 = Button(root,text="Average",command=calcAverage)
button2.grid(row=6,column=1)
button3 = Button(root,text="Quit",command=root.destroy)
button3.grid(row=6,column=2)
    
