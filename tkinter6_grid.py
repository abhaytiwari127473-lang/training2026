from tkinter import *
root=Tk()
root.title("My Calci")
lbl=Label(root,text="Enter first number",
          font=("Comic Sans Ms", 15, "bold"),
          bg="black", fg="white"
          )
lbl.grid(row=0,column=0)
a=IntVar()
input1=Entry(root,textvariable=a,font=("Comic Sans Ms", 15, "bold"),
         )
input1.grid(row=0,column=1)
lbl1=Label(root,text="Enter first number",
          font=("Comic Sans Ms", 15, "bold"),
          bg="black", fg="white"
          )
lbl1.grid(row=1,column=0)
b=IntVar()
input2=Entry(root,textvariable=b,font=("Comic Sans Ms", 15, "bold"),
         )
input2.grid(row=1,column=1)

btn=Button(root,font=("Comic Sans Ms",15,"bold"),text="Show2 ",
           bg="red",fg="white")
btn.grid(row=2,columnspan=2)
root.mainloop()