#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import messagebox

def send_mail():
    recipient = recipient_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", tk.END)
    
    # Code to send the email goes here
    # Replace the print statement with your email sending logic
    
    print("Sending email...")
    print("Recipient: ", recipient)
    print("Subject: ", subject)
    print("Message: ", message)
    
    messagebox.showinfo("Success", "Email sent successfully!")

# Create the main window
window = tk.Tk()
window.title("Mail Application")

# Create labels
recipient_label = tk.Label(window, text="Recipient:")
subject_label = tk.Label(window, text="Subject:")
message_label = tk.Label(window, text="Message:")

# Create entry fields
recipient_entry = tk.Entry(window)
subject_entry = tk.Entry(window)
message_text = tk.Text(window, height=10, width=30)

# Create send button
send_button = tk.Button(window, text="Send", command=send_mail)

# Grid layout
recipient_label.grid(row=0, column=0)
subject_label.grid(row=1, column=0)
message_label.grid(row=2, column=0)

recipient_entry.grid(row=0, column=1)
subject_entry.grid(row=1, column=1)
message_text.grid(row=2, column=1)

send_button.grid(row=3, column=1, pady=10)

# Start the main loop
window.mainloop()

