import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont

def validate_credit_card_input(*args):
    credit_card = credit_card_entry.get()
    formatted_credit_card = credit_card.replace("-", "").replace(" ", "")[:16]  # Cap the card number to 16 characters
    
    # Format the credit card number with hyphens
    formatted_credit_card = "-".join(formatted_credit_card[i:i+4] for i in range(0, len(formatted_credit_card), 4))
    
    # Update the credit card entry with the formatted number
    credit_card_entry.delete(0, tk.END)
    credit_card_entry.insert(0, formatted_credit_card)

def show_user_info():
    name = name_entry.get()
    age = age_entry.get()
    credit_card = credit_card_entry.get()
    
    if name.strip() == "" or age.strip() == "" or credit_card.strip() == "":
        messagebox.showerror("Error", "Oops! It seems you forgot to enter your name, age, or credit card information.")
    else:
        messagebox.showinfo("User Info", "Name: {}\nAge: {}\nCredit Card: {}\n\nGreat job, {}! YOU JUST GAVE YOUR CARD INFO TO ME!!!".format(name, age, credit_card, name))
    
    # Clear the entry fields
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    credit_card_entry.delete(0, tk.END)

def about():
    messagebox.showinfo("About", "This is a program to simply take user's credit card information. Not sure who it would work on, but I'd hope somebody.")

def methods():
    messagebox.showinfo("Methods", "Ways to make this program even worse:\n\n- Save the card information to a database.\n- Check and validate only valid card numbers using the accepted algorithm per card and checking against that.")

def close_program():
    if name_entry.get().strip() == "" or age_entry.get().strip() == "" or credit_card_entry.get().strip() == "":
        messagebox.showinfo("Smart Move", "Smart move! You didn't enter your information!")
        window.destroy()
    else:
        messagebox.showinfo("Goodbye", "Closing the program...")
        window.destroy()
        
def change_color():
    color = next(colors)
    rainbow_label.config(foreground=color)
    rainbow_label.after(200, change_color)
    

# Create the main tkinter window
window = tk.Tk()
window.title("User Information")
window.geometry("500x500")  # Set the window size
window.configure(bg="#F8F8F8")  # Set the background color to dark gray

# Set the font style for the buttons
button_font = tkfont.Font(family="Arial", size=14)

# Create and pack the labels and entry fields

#RAINBOW LABEL LOL THANKS GOOGLE
rainbow_label = tk.Label(window, text="By: Branden Munar", font=("Arial", 18, "bold"))
rainbow_label.pack(pady=10)

colors = iter(["red", "orange", "yellow", "green", "blue", "indigo", "violet"])
change_color()

name_label = tk.Label(window, text="Name:", font=button_font)
name_label.pack()
name_entry = tk.Entry(window, font=button_font)
name_entry.pack()

age_label = tk.Label(window, text="Age:", font=button_font)
age_label.pack()
age_entry = tk.Entry(window, font=button_font)
age_entry.pack()

credit_card_label = tk.Label(window, text="Credit Card:", font=button_font)
credit_card_label.pack()

# Create and pack the credit card entry field
credit_card_entry = tk.Entry(window, font=button_font)
credit_card_entry.bind("<KeyRelease>", validate_credit_card_input)
credit_card_entry.pack()

# Create and pack the buttons
submit_button = tk.Button(window, text="Submit", command=show_user_info, font=button_font, bg="green", fg="white")
submit_button.pack(pady=10)

about_button = tk.Button(window, text="About", command=about, font=button_font, bg="blue", fg="white")
about_button.pack(pady=5)

methods_button = tk.Button(window, text="Methods", command=methods, font=button_font, bg="purple", fg="white")
methods_button.pack(pady=5)

close_button = tk.Button(window, text="Close", command=close_program, font=button_font, bg="red", fg="white")
close_button.pack(pady=5)

# Start the tkinter event loop
window.mainloop()
