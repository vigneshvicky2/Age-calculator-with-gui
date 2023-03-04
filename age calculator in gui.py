#import all necessary modules 
import tkinter
from datetime import date
from tkinter import messagebox
from tkinter import*
from PIL import ImageTk,Image
#creating background image
bago=Tk()
bago.title("testing gui")
#put your background image file path
img=Image.open('F:\\win 10 wallpapers\\magenta.png')
bc=ImageTk.PhotoImage(img)
bago.geometry('1024x768')
lbl=Label(bago,image=bc)
lbl.place(x=0,y=0)
#defining age calculation program
def calc():
   name=lnb.get() 
   dob=ent.get() 
   birthdate = date.fromisoformat(dob)
   today=date.today()
   age=today.year - birthdate.year - ((today.month,today.day)<(birthdate.month, birthdate.day))
   messagebox.showinfo("age calculator ","Hi "+name+" your age is: "+str(age))
#creating heading of program 
tit=tkinter.Label(bago,text="AGE CALCULATOR",font=("arial",30))
tit.place(x=368,y=50)
#creating label with enter your name
unb=tkinter.Label(bago,text="enter your name: ",font=("arial",19))
unb.place(x=100,y=150)
#creating name entry
lnb=tkinter.Entry(bago,font=("arial",19))
lnb.place(x=400,y=150)
#creating dob entry
age_1=tkinter.Label(bago,text="enter your DOB: ",font=("arial",19))
age_1.place(x=100,y=250)
ent=tkinter.Entry(bago,font=("arial",19))
ent.place(x=400,y=250)
#creating button
but1=tkinter.Button(bago,text="calculate",command=calc,font=('arial',15))
but1.place(x=500,y=400)
#creating credits
lnb1=tkinter.Label(bago,text="THIS PROGRAM IS CREATED BY VIGNESH",font=("arial",19))
lnb1.place(x=250,y=500)
bago.mainloop


