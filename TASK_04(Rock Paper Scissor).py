from tkinter import *
import random
def game(user_choice):
    global com,you
    choices=[1,2,3]
    com_choice=random.choice(choices)
    if com_choice == user_choice:
        status.set("It's Tie")
    elif com_choice == 3 and user_choice == 1:
        status.set("YOU WIN "+("\U0001F3C6"*2))
        you=you+1
    elif com_choice==2 and user_choice == 3:
        status.set("YOU WIN "+("\U0001F3C6"*2))
        you=you+1        
    elif com_choice ==1 and user_choice == 2:
        status.set("YOU WIN "+("\U0001F3C6"*2))
        you=you+1
    else:
        status.set("YOU LOSE "+("\U0001F61E"*2))
        com=com+1
    comp_win.configure(text=f"Computer: {com}")
    you_win.configure(text=f"You: {you}")    

window=Tk()
com=0
you=0
window.geometry("425x360+400+200")
window.configure(bg="light yellow")
window.title("ROCK<-->PAPER<-->SCISSOR")
window.resizable(False,False)
status=StringVar()
status.set("")
heading=Label(window,text="Rock<-->Paper<-->Scissor",width=25,bg="light yellow",fg="dark blue",font=("Lucida calligraphy",20,"bold","italic","underline"))
heading.grid(row=0,column=0,columnspan=8,pady=20,padx=2,stick="news")
rock=(PhotoImage(file="rock.png")).subsample(5,6)
paper=PhotoImage(file="paper.png").subsample(5,6)
scissor=PhotoImage(file="scissors.png").subsample(5,6)
rockprint=Label(window,text="ROCK",bg="light yellow",fg="dark blue",font=("Arial",16,"bold","underline"))
rockprint.grid(row=2,column=0,columnspan=2,padx=30,sticky="news")
paperprint=Label(window,text="PAPER",bg="light yellow",fg="dark blue",font=("Arial",16,"bold","underline"))
paperprint.grid(row=2,column=4,columnspan=2,padx=30,sticky="news")
scissorprint=Label(window,text="SCISSOR",bg="light yellow",fg="dark blue",font=("Arial",16,"bold","underline"))
scissorprint.grid(row=2,column=2,columnspan=2,padx=30,sticky="news")
rock_button=Button(window,image=rock,bg="light yellow",command=lambda : game(1))
rock_button.grid(row=1,column=0,columnspan=2,padx=30,pady=15,sticky="news")
scissor_button=Button(window,image=scissor,bg="light yellow",command=lambda : game(3))
scissor_button.grid(row=1,column=2,columnspan=2,padx=30,pady=15,sticky="news")
paper_button=Button(window,image=paper,bg="light yellow",command=lambda : game(2))
paper_button.grid(row=1,column=4,columnspan=2,padx=30,pady=15,sticky="news")
display=Label(window,textvariable=status,bg="dark blue",fg="light yellow",font=("Lucida",20,"bold","italic"))
display.grid(row=3,column=0,columnspan=6,pady=25,sticky="news")
comp_win=Label(window,text="Computer: ",bg="light yellow",fg="dark blue",font=("Arial",10,"bold"))
comp_win.grid(row=4,column=0,columnspan=2,padx=5,pady=5,sticky="news")
you_win=Label(window,text="You: ",bg="light yellow",fg="dark blue",font=("Arial",10,"bold"))
you_win.grid(row=5,column=0,columnspan=2,padx=1,pady=3,sticky="news")
window.mainloop()
