from tkinter import * 
import random
import string

def password_generator(num, option):
    if option == "Strong":
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.sample(characters, num))
    elif option == "Weak":
        characters = string.ascii_letters
        password = "".join(random.sample(characters, num))
    else:
        password = "Please select the type"        
    return password

def generate_password():
    num = int(input_entry.get())
    selected_option = var.get()
    password = password_generator(num, selected_option)
    if len(password) <= 15:
        display.config(text=f"Password: {password}")
    else:
        display.config(text="Error: password limit is 15")    

window = Tk()
window.geometry("400x300+400+200")
window.title("PASSWORD GENERATOR")
window.configure(bg="navy blue")

title = Label(window, bg="black", width=23, text="Password Generator", font=("phobos", 20, "bold"))
title.configure(fg="White")
title.grid(row=0, column=0, columnspan=6, padx=1, pady=20, sticky="news")

length = Label(window, bg="navy blue", fg="White", text="Length:", font=("Arial", 15, "bold"))
length.grid(row=1, column=0, columnspan=2, padx=2, pady=10, sticky="news")

input_entry = Entry(window, width=2, font=("Arial", 15, "bold"), bg="dark grey", fg="Black")
input_entry.grid(row=1, column=2, columnspan=1, padx=2, pady=10, sticky="news")

var = StringVar()
var.set(None) 
strong = Radiobutton(window, text="Strong", variable=var, value="Strong")
strong.grid(row=1, column=4, columnspan=1, padx=2, pady=10, sticky="news")
weak = Radiobutton(window, text="Weak", variable=var, value="Weak")
weak.grid(row=1, column=5, columnspan=1, padx=2, pady=10, sticky="news")

generate_button = Button(window, text="Generate", bg="White", fg="Black", font=("Arial", 15, "bold"), command=generate_password)
generate_button.grid(row=5, column=0, columnspan=6,pady=20, sticky="news")

display = Label(window, text="Password: ", bg="navy blue", fg="White", font=("Arial", 15, "bold"))
display.grid(row=6, column=0, columnspan=6, padx=2, pady=10, sticky="news")

window.mainloop()
