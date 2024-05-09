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

#Define functions for button clicks, clearing the entry, calculating the result, and asking to continue
def button_click(number):
    main_entry.insert(END, number)

def clear():
    main_entry.delete(0, END)

def calculate():
    try:
        equation = main_entry.get()
        new_equation = equation.replace("X", "*")
        result = eval(new_equation)
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
        messagebox.showinfo("Thanks for Trying the Program", "Thank You!")
        app.after(4000, app.destroy)
#Create result box (entry)
main_entry = customtkinter.CTkEntry(app, width=280, height=50, fg_color= "#66CDAA", text_color="white",)
main_entry.place(x=10, y=10)
#Create buttons for numbers and operators
#Create calculate button
#Create clear button
#Start the GUI event loop