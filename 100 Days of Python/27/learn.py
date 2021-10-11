from tkinter import *
window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)
def button_clicked():
    textt = input.get()
    label.config(text=textt)


#Label
label = Label(text="I am a label",font=('Arial', 24,"bold"))
# label.pack()
# label.place(x=90,y=0)
label.grid(column=0,row=0)

#Button
button = Button(text = "Click me", command = button_clicked)
button.grid(column=1, row=1)

button1 = Button(text= "click me", command= button_clicked)
button1.grid(column=0,row=3)

#Entry
input = Entry(width=10)
# input.pack()
print(input.get())
input.grid(column=3,row=4)


window.mainloop()