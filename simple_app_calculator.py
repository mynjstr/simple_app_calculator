#Import necessary tkinter libraries
import customtkinter
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import time

#Set GUI theme and window size
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.title("Simple Calculator App")
app.geometry("300x300")
app.resizable(False, False)

#Define functions for button clicks, clearing the entry, calculating the result, and asking to continue
def button_click(number):
    main_entry.insert(END, number)

def clear():
    main_entry.delete(0, END)

def calculate():
    try:
        equation = main_entry.get()
        user_equation = equation.replace("X", "*")
        if any(character.isalpha() for character in user_equation):
            raise ValueError
        result = eval(user_equation)
        clear()
        main_entry.insert(0, result)
    except ZeroDivisionError:
        messagebox.showerror("ERROR", "Dividing by 0 is not possible.")
    except (ValueError, TypeError):
        messagebox.showerror("ERROR", "Kindly provide valid values.")
    finally:
        ask_to_continue()

def ask_to_continue():
    response = messagebox.askyesno("Continue?", "Do you want to continue?")
    if response:
        clear()
    else:
        messagebox.showinfo("Thanks for Trying ", "Thank You!")
        app.after(4000, app.destroy)

#Create result box (entry)
main_entry = customtkinter.CTkEntry(app, width=280, height=50, fg_color= "#66CDAA", text_color="white",)
main_entry.place(x=10, y=10)

#Create buttons for numbers and operators
buttons = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9',
    '0', '.', 
    '+', '-', 'X', '/'
]

x_values = [15, 85, 155, 15, 85, 155, 15, 85, 155, 15, 85, 225, 225, 225, 225]
y_values = [170, 170, 170, 125, 125, 125, 80, 80, 80, 215, 215, 80, 125, 170, 215]

for i, button_text in enumerate(buttons):
    button = customtkinter.CTkButton(app, text=button_text, command=lambda text=button_text: button_click(text), width=60)
    button.place(x=x_values[i], y=y_values[i])

#Create calculate button
calculate_button = customtkinter.CTkButton(app, command=calculate, text="=", width=270)
calculate_button.place(x=15, y=255)

#Create clear button
clear_button = customtkinter.CTkButton(app, text="C", command=ask_to_continue, width=60)
clear_button.place(x=155, y=215)

#Start the GUI event loop
app.mainloop()