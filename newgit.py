import tkinter as tk
import requests
import random
import pyperclip

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

    email_text += "Please feel free to reach out to us at any time!\n\n"

    quote = fetch_quote()
    email_text += quote

    email_text_box.delete("1.0", tk.END)
    email_text_box.insert(tk.END, email_text)

def copy_to_clipboard():
    email_text = email_text_box.get("1.0", tk.END)
    pyperclip.copy(email_text)

# Create GUI
root = tk.Tk()
root.title("Email Generator")

# Logo
logo_image = tk.PhotoImage(file="/Users/rohitasil/Documents/code base/dispatch_email_logi-removebg-preview.png")
logo_label = tk.Label(root, image=logo_image)
logo_label.pack(side=tk.LEFT, padx=10, pady=10)

# Heading
heading_label = tk.Label(root, text="Dispatch Email Generator", font=("Arial", 16, "bold"))
heading_label.pack(pady=10)

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

email_text_box = tk.Text(right_frame, height=15, width=50)
email_text_box.pack()

# Generate Button
generate_button = tk.Button(left_frame, text="Generate Email", command=generate_email)
generate_button.pack(pady=10)

# Copy to Clipboard Button
copy_button = tk.Button(left_frame, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack()

# Run the GUI
root.mainloop()
