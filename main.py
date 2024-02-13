import tkinter as tk
import time

app = tk.Tk()
app.title("Digital Clock")
app.geometry("300x100")
app.resizable(1, 1)

label = tk.Label(app, font=("Arial", 30, 'bold'), bg="black", fg="white")
label.pack(fill="both", expand=1)

def digital_clock():
    text_input = time.strftime("%H:%M:%S %p")
    label.config(text=text_input)
    label.after(200, digital_clock)

digital_clock()
app.mainloop()