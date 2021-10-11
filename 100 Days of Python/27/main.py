from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=400, height=200)
window.config(padx=20, pady=20)

def mile_to_km():
    answer = float(miles_input.get())
    answer1 = round(answer*1.60934, 3)
    kilo_res_label.config(text=answer1)

# label

miles_label = Label(text=" Miles")
miles_label.grid(column =2,row=0)
is_equal = Label(text="is equal to")
is_equal.grid(column=0 ,row=1)
kilo_res_label = Label(text='0')
kilo_res_label.grid(column=1 ,row=1)
kilo_label = Label(text="Km")
kilo_label.grid(column=2,row=1)

# Entry
miles_input = Entry()
miles_input.grid(column=1 ,row=0)
miles_input.get()

# button
calculate = Button(text='Calculate', command = mile_to_km)
calculate.grid(column=1,row=2)

window.mainloop()
