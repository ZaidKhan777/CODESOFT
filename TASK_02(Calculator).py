from tkinter import *
import math as mt
ans=None
def button_click(symbol):
    global ans
    if symbol == '=':
        try:
            result=eval(display.get())
            display.delete(0,END)
            display.insert(END,result)
            ans=result
        except Exception as e:
            display.delete(0,END)
            display.insert(END,"Erorr")
            ans=None
    elif symbol == '√':
        try:
            num=float(display.get())
            display.delete(0,END)
            result=mt.sqrt(num)
            display.insert(END,str(result))
            ans=result
        except Exception as e:
            display.delete(0,END)
            display.insert(END,"Erorr")
            ans=None  
    elif symbol == '□²':
        try:
            num = int(display.get())
            display.delete(0,END)
            result=mt.pow(num,2)
            display.insert(END,str(result))
            ans=result
        except Exception as e:
            display.delete(0,END)
            display.insert(END,"Erorr")
            ans=None    
    elif symbol == 'Ans':
        if ans is not None:
            display.insert(END,str(ans))
                            
    elif symbol == 'C':
        display.delete(0,END)
    else:
        current=display.get()
        display.delete(0,END)
        if current=="Erorr":
            display.delete(0,END)
        display.insert(END,str(current)+str(symbol))        

window = Tk()
window.title("CALCULATOR")
window.geometry("340x361+400+200")
window.configure(bg="light grey")
window.resizable(False,False)

display = Entry(window,width=20, font=("Arial", 20, "bold"))
display.grid(row=0, column=0, columnspan=4, padx=20, pady=20, sticky="news")

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0), ('√', 5, 1), ('□²', 5, 2), ('Ans', 5, 3)
]
for symbol,rows,columns in buttons:
        if symbol == '+' or symbol == '-' or symbol == '*' or symbol == '/':
             button= Button(window,text=symbol,font=("Lucida",14,"bold"),padx=10,pady=10,bg="light green",command=lambda s=symbol:button_click(s))
        elif symbol == 'Ans' or symbol == '=':
             button= Button(window,text=symbol,font=("Lucida",14,"bold"),padx=10,pady=10,bg="light yellow",command=lambda s=symbol:button_click(s))
        elif symbol == '√' or symbol == '□²':
            button= Button(window,text=symbol,font=("Lucida",14,"bold"),padx=10,pady=10,bg="light pink",command=lambda s=symbol:button_click(s))     
        else:        
            button= Button(window,text=symbol,font=("Lucida",14,"bold"),padx=10,pady=10,bg="light blue",command=lambda s=symbol:button_click(s))
        button.grid(row=rows,column=columns,sticky="news")
                
window.mainloop()
