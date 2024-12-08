from tkinter import *

root = Tk()
root.title("Calculator")
expression = str("")
def BtnClicked(number):
    global expression 
    expression += number
    e.delete(0,END)
    e.insert(0,expression)

def equalClicked():
    global expression
    try:
        x = eval(expression)
        e.delete(0, END)
        e.insert(0, x)
        expression = ""
    except Exception as error:
        e.delete(0, END)
        e.insert(0, "Error")
        expression = ""
def ClrClicked():
    global expression
    e.delete(0,END)
    expression = ""

# Entry widget for displaying calculations
e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=15)

# Define buttons
button_0 = Button(root, text="0", width=10,command= lambda:BtnClicked("0"))
button_1 = Button(root, text="1", width=10,command= lambda:BtnClicked("1"))
button_2 = Button(root, text="2", width=10,command= lambda:BtnClicked("2"))
button_3 = Button(root, text="3", width=10,command= lambda:BtnClicked("3"))
button_4 = Button(root, text="4", width=10,command= lambda:BtnClicked("4"))
button_5 = Button(root, text="5", width=10,command= lambda:BtnClicked("5"))
button_6 = Button(root, text="6", width=10,command= lambda:BtnClicked("6"))
button_7 = Button(root, text="7", width=10,command= lambda:BtnClicked("7"))
button_8 = Button(root, text="8", width=10,command= lambda:BtnClicked("8"))
button_9 = Button(root, text="9", width=10,command= lambda:BtnClicked("9"))
button_multiplication = Button(root, text="*", width=10, command= lambda:BtnClicked("*"))
button_division = Button(root, text="/", width=10, command= lambda:BtnClicked("/"))
button_addition = Button(root, text="+", width=10, command= lambda:BtnClicked("+"))
button_subtraction = Button(root, text="-", width=10, command= lambda:BtnClicked("-"))
button_Equal = Button(root, text="=", width=10, command= lambda:equalClicked())
button_Clr = Button(root, text="Clr", width=10, command= lambda:ClrClicked())

# Organize buttons in a grid layout
button_7.grid(row=1, column=0, padx=10, pady=10)
button_8.grid(row=1, column=1, padx=10, pady=10)
button_9.grid(row=1, column=2, padx=10, pady=10)

button_4.grid(row=2, column=0, padx=10, pady=10)
button_5.grid(row=2, column=1, padx=10, pady=10)
button_6.grid(row=2, column=2, padx=10, pady=10)

button_1.grid(row=3, column=0, padx=10, pady=10)
button_2.grid(row=3, column=1, padx=10, pady=10)
button_3.grid(row=3, column=2, padx=10, pady=10)

button_0.grid(row=4, column=1, padx=10, pady=10)
button_Clr.grid(row=4, column=0, padx=10, pady=10)

button_division.grid(row=1, column=3, padx=10, pady=10)
button_multiplication.grid(row=2, column=3, padx=10, pady=10)
button_addition.grid(row=3, column=3, padx=10, pady=10)
button_subtraction.grid(row=4, column=3, padx=10, pady=10)

button_Equal.grid(row=4, column=2, padx=10, pady=10)

root.mainloop()
