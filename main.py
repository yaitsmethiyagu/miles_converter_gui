from tkinter import *

window = Tk()

window.title('Miles to Kilometer converter')

window.minsize(width=200, height= 300)
window.config(padx=20, pady= 20)

def convert():
    miles = user_input.get()
    if miles.isdigit():
        km = int(miles) * 1.609344
        km = round(km, 2)
        result.config(text= str(km), font=("courier", 20, "bold"))


user_input = Entry()


miles = Label(text="miles")
miles.config(padx=20, pady= 20)

is_equal_to = Label(text= "is equal to")
is_equal_to.config(padx=20, pady= 20)

result = Label(text="-----", font=("courier", 20, "bold"))
result.config(padx=20, pady= 20)

km = Label(text="KM")
km.config(padx=20, pady= 20)

calculate = Button(text= "Calculate", command= convert)
calculate.config(padx=20, pady= 20)

user_input.grid(column= 1, row= 0)
miles.grid(column=2, row=0)
is_equal_to.grid(column=0, row=1)
result.grid(column=1, row= 1)
km.grid(column=2, row=1)
calculate.grid(column=1, row=2)



window.mainloop()