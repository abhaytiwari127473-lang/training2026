from tkinter import *
def left_click(event=''):
    print("Left button is clicked")
def right_click(event=''):
    print("Right button is clicked")

def middle_click(event=''):
    print("Middle button is clicked")
root=Tk()

root.title("My Calci")
btn_left=Button(root,font=("Comic Sans Ms",15,"bold"),text="Left button",
           bg="black",fg="white",command=left_click)
btn_left.pack()


btn_middle=Button(root,font=("Comic Sans Ms",15,"bold"),text="Middle button ",
           bg="blue",fg="white",command=middle_click)
btn_middle.pack()

btn_right=Button(root,font=("Comic Sans Ms",15,"bold"),text="Right Button",
           bg="red",fg="white",command=right_click)
btn_right.pack()

root.bind("<Control-s>",left_click)
root.bind("<Control-2>",middle_click)
root.bind("<Control-3>",right_click)





root.geometry("400x400+400+200")
root.wm_iconbitmap("calci.ico")
#root.resizable(0,0,)
root.mainloop()