from tkinter import *

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" I couldn't understand that! ")
        expression = ""
 

def clear():
    global expression
    expression = ""
    equation.set("")
 
 
if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="black")
    gui.title("Calculator")
    gui.geometry("380x255")
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation, bd = 0, bg = "#f7ffff", font = ("Helvetica", 24))
    expression_field.grid(columnspan=4, pady = 10, padx = 10)
    
    button1 = Button(gui, text=' 7 ', fg='white', bg='#a8a8a8',
                    command=lambda: press(7), height=2, width=10, bd = 0, font = ("default", 9, "bold"))
    button1.grid(row=2, column=0)
 
    button2 = Button(gui, text=' 8 ', fg='white', bg='#a8a8a8',
                    command=lambda: press(8), height=2, width=10, bd = 0, font = ("default", 9, "bold"))
    button2.grid(row=2, column=1)
 
    button3 = Button(gui, text=' 9 ', fg='white', bg='#a8a8a8',
                    command=lambda: press(9), height=2, width=10, bd = 0, font = ("default", 9, "bold"))
    button3.grid(row=2, column=2)
 
    button4 = Button(gui, text=' 4 ', fg='white', bg='#a8a8a8',
                    command=lambda: press(4), height=2, width=10, bd = 0, font = ("default", 9, "bold"))
    button4.grid(row=3, column=0)
 
    button5 = Button(gui, text=' 5 ', fg='white', bg='#a8a8a8',
                    command=lambda: press(5), height=2, width=10, bd = 0, font = ("default", 9, "bold"))
    button5.grid(row=3, column=1)
 
    button6 = Button(gui, text=' 6 ', fg='white', bg='#a8a8a8',
                    command=lambda: press(6), height=2, width=10, bd = 0, font = ("default", 9, "bold"))
    button6.grid(row=3, column=2)
 
    button7 = Button(gui, text=' 1 ', fg='white', bg='#a8a8a8',
                    command=lambda: press(1), height=2, width=10, bd = 0, font = ("default", 9, "bold"))
    button7.grid(row=4, column=0)
 
    button8 = Button(gui, text=' 2 ', fg='white', bg='#a8a8a8',
                    command=lambda: press(2), height=2, width=10, bd = 0, font = ("default", 9, "bold"))
    button8.grid(row=4, column=1)
 
    button9 = Button(gui, text=' 3 ', fg='white', bg='#a8a8a8',
                    command=lambda: press(3), height=2, width=10, bd = 0, font = ("default", 9, "bold"))
    button9.grid(row=4, column=2)
 
    button0 = Button(gui, text=' 0 ', fg='white', bg='#a8a8a8',
                    command=lambda: press(0), height=2, width=10, bd = 0, font = ("default", 9, "bold"))
    button0.grid(row=5, column=0)
 
    plus = Button(gui, text=' + ', fg='white', bg='#2e2e2e',
                command=lambda: press("+"), height=2, width=10, bd = 0, font = ("default", 9, "bold"))
    plus.grid(row=2, column=3)
 
    minus = Button(gui, text=' - ', fg='white', bg='#2e2e2e',
                command=lambda: press("-"), height=2, width=10, bd = 0, font = ("default", 9, "bold"))
    minus.grid(row=3, column=3)
 
    multiply = Button(gui, text=' * ', fg='white', bg='#2e2e2e',
                    command=lambda: press("*"), height=2, width=10, bd = 0, font = ("default", 9, "bold"))
    multiply.grid(row=4, column=3)
 
    divide = Button(gui, text=' / ', fg='white', bg='#2e2e2e',
                    command=lambda: press("/"), height=2, width=10, bd = 0, font = ("default", 9, "bold"))
    divide.grid(row=5, column=3)
 
    equal = Button(gui, text=' = ', fg='white', bg='#ff6214',
                command=equalpress, height=2, width=10, bd = 0, font = ("default", 9, "bold"))
    equal.grid(row=5, column=2)
 
 
    Decimal= Button(gui, text='.', fg='white', bg='#a8a8a8',
                    command=lambda: press('.'), height=2, width=10, bd = 0, font = ("default", 9, "bold"))
    Decimal.grid(row=5, column=1)

    clear = Button(gui, text='Clear', fg='white', bg='#2e2e2e',
                command=clear, height=2, width=51, bd = 0, font = ("default", 9, "bold"))
    clear.grid(columnspan=4, pady = 5)
    gui.mainloop()

