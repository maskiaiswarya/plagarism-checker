from difflib import SequenceMatcher
from tkinter import *

def display():
        with open("file1.txt") as file1, open("file2.txt") as file2:
          data1=file1.read()
          data2=file2.read()
          plagiarism_ratio=SequenceMatcher(None,data1,data2).ratio()
          print(plagiarism_ratio)
a=Tk()
a.configure(background='light pink')
heading=Label(a,text='PLAGARISM CHECKER',fg="blue",bg="pink",font=("Times",15,'bold'))
heading.pack(side=TOP)
a.geometry('250x150')
App=Button(a,text='check here',width=10,font=('Times',10,'bold'),command=display)
App.place(x=100,y=40)
a.mainloop()
