import tkinter as tk
from tkinter import messagebox
import requests
import random

def fetch_quote():
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        quote_data = response.json()
        quote = quote_data["content"]
        author = quote_data["author"]
        return f"{quote} - {author}"
    else:
        return "Failed to fetch a quote."

def generate_email():
    customer_name = name_entry.get()
    tracking_id = id_entry.get()
    shipment_name = shipment_entry.get()
    tracking_link = link_entry.get()

    email_text = f"Dear {customer_name},\n\n"
    email_text += "We are pleased to inform you that your shipment, '{}', with tracking ID '{}' has been dispatched.\n".format(shipment_name, tracking_id)
    email_text += "You can track your shipment by clicking on the following link:\n"
    email_text += tracking_link + "\n\n"

    quote = fetch_quote()
    email_text += quote

    messagebox.showinfo("Email Text", email_text)

# Create GUI
root = tk.Tk()
root.title("Email Generator")

# Labels
name_label = tk.Label(root, text="Customer Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

id_label = tk.Label(root, text="Tracking ID:")
id_label.pack()
id_entry = tk.Entry(root)
id_entry.pack()

shipment_label = tk.Label(root, text="Shipment Name:")
shipment_label.pack()
shipment_entry = tk.Entry(root)
shipment_entry.pack()

link_label = tk.Label(root, text="Tracking Link:")
link_label.pack()
link_entry = tk.Entry(root)
link_entry.pack()

# Button
generate_button = tk.Button(root, text="Generate Email", command=generate_email)
generate_button.pack()

# Run the GUI
root.mainloop()
