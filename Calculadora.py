from tkinter import *
import parser 
root = Tk ()
root.title("Calcuchino")

display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

i = 0


def _mostrarnumero(n):
    global i
    display.insert(i, n)
    i+=1

def _operaciones(operator):
    global i
    operator_lenght = len(operator)
    display.insert(i, operator)
    i+=operator_lenght

def clear_display():
    display.delete(0, END)

def undo():
    display_state=display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clear_display()
        display.insert(0, display_new_state)
    else:
        clear_display()
        display.insert(0, "error")

def calcular():
    math_expression = display_state = display.get()
    try:
        parser.expr(display_state).compile()
        result = eval(math_expression)
        clear_display()
        display.insert(0, result)
    except expression as identifier:
        clear_display()
        display.insert(0, "error")

#Button
Button(root, text="1", command=lambda :_mostrarnumero(1)).grid(row=2, column=0, sticky=W+E)
Button(root, text="2", command=lambda :_mostrarnumero(2)).grid(row=2, column=1, sticky=W+E)
Button(root, text="3", command=lambda :_mostrarnumero(3)).grid(row=2, column=2, sticky=W+E)

Button(root, text="4", command=lambda :_mostrarnumero(4)).grid(row=3, column=0, sticky=W+E)
Button(root, text="5", command=lambda :_mostrarnumero(5)).grid(row=3, column=1, sticky=W+E)
Button(root, text="6", command=lambda :_mostrarnumero(6)).grid(row=3, column=2, sticky=W+E)

Button(root, text="7", command=lambda :_mostrarnumero(7)).grid(row=4, column=0, sticky=W+E)
Button(root, text="8", command=lambda :_mostrarnumero(8)).grid(row=4, column=1, sticky=W+E)
Button(root, text="9", command=lambda :_mostrarnumero(9)).grid(row=4, column=2, sticky=W+E)


Button(root, text="AC",command=lambda: clear_display()).grid(row=5, column=0, sticky=W+E)
Button(root, text="0", command=lambda :_mostrarnumero("0")).grid(row=5, column=1, sticky=W+E)
Button(root, text="%",command=lambda: _operaciones("%")).grid(row=5, column=2, sticky=W+E)

Button(root, text="/",command=lambda: _operaciones("/")).grid(row=2, column=3, sticky=W+E)
Button(root, text="*",command=lambda: _operaciones("*")).grid(row=3, column=3, sticky=W+E)
Button(root, text="-",command=lambda: _operaciones("-")).grid(row=4, column=3, sticky=W+E)
Button(root, text="+",command=lambda: _operaciones("+")).grid(row=5, column=3, sticky=W+E)

Button(root, text="⬅",command=lambda: undo()).grid(row=2, column=4, sticky=W+E , columnspan = 2)
Button(root, text="exp",command=lambda: _operaciones("**")).grid(row=3, column=4, sticky=W+E)
Button(root, text="^2",command=lambda: _operaciones("**2")).grid(row=3, column=5, sticky=W+E)
Button(root, text="(",command=lambda: _operaciones("(")).grid(row=4, column=4, sticky=W+E)
Button(root, text=")",command=lambda: _operaciones(")")).grid(row=4, column=5,  sticky=W+E)
Button(root, text="=",command=lambda: calcular()).grid(row=5, column=4, sticky=W+E, columnspan = 2)










root.mainloop()