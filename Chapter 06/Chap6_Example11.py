from tkinter import *  
  
myroot = Tk()  
myroot.geometry("300x300")  
myroot.title('Main window')
mytopobj = Toplevel(myroot)

mytopobj.title('New window')

mytopobj.geometry("300x300")  
myroot.lift(mytopobj)

# infinitely running mainloop  
myroot.mainloop() 
