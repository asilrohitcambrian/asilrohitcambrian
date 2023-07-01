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

    email_text_box.delete("1.0", tk.END)
    email_text_box.insert(tk.END, email_text)

# Create GUI
root = tk.Tk()
root.title("Email Generator")

# Left Frame (Input Boxes)
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, padx=10, pady=10)

name_label = tk.Label(left_frame, text="Customer Name:")
name_label.pack()
name_entry = tk.Entry(left_frame)
name_entry.pack()

id_label = tk.Label(left_frame, text="Tracking ID:")
id_label.pack()
id_entry = tk.Entry(left_frame)
id_entry.pack()

shipment_label = tk.Label(left_frame, text="Shipment Name:")
shipment_label.pack()
shipment_entry = tk.Entry(left_frame)
shipment_entry.pack()

link_label = tk.Label(left_frame, text="Tracking Link:")
link_label.pack()
link_entry = tk.Entry(left_frame)
link_entry.pack()

# Right Frame (Email Text Box)
right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

email_text_label = tk.Label(right_frame, text="Email Text:")
email_text_label.pack()

email_text_box = tk.Text(right_frame, height=100, width=100)
email_text_box.pack()

# Generate Button
generate_button = tk.Button(left_frame, text="Generate Email", command=generate_email)
generate_button.pack(pady=10)

# Image
unicorn_image = tk.PhotoImage(file="/Users/rohitasil/Documents/code base/unicorn.png")
unicorn_label = tk.Label(right_frame, image=unicorn_image)
unicorn_label.pack(side=tk.BOTTOM, padx=10, pady=10)

# Run the GUI
root.mainloop()
