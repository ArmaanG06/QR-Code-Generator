import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk
import qrcode.constants

#Creates the main app window
def create_main_window():
    window = tk.Tk()
    window.title("QR Code Generator")
    window.geometry("500x500")
    window.resizable(False, False)
    return window

#Function that creates the QR code
def generate_qr():
    data = entry.get()
    if not data:
        messagebox.showerror("Error", "Please enter text or a URL!")
        return

    # Generates the QR code using qrcode library, contols the size of the code 
    qr = qrcode.QRCode(
        version=1,  
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    #Creates an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    #Save the image temporarily to display it in Tkinter
    img.save("temp_qr.png")

    #Update the label to show the new QR code
    qr_image = Image.open("temp_qr.png")
    qr_photo = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo

#Function to save the qr code
def save_qr():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
    )
    if file_path:
        try:
            img = Image.open("temp_qr.png")
            img.save(file_path)
            messagebox.showinfo("Success", f"QR code saved to {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save QR code: {e}")

#Create GUI
window = create_main_window()

#Create input feild for text/url
label = tk.Label(window, text="Enter text or URL:", font=("Arial", 14))
label.pack(pady=10)
entry = tk.Entry(window, font=("Arial", 14), width=30)
entry.pack(pady=10)

# Button to generate the QR code
generate_button = tk.Button(window, text="Generate QR Code", font=("Arial", 14), command=generate_qr)
generate_button.pack(pady=10)

# Label to display the generated QR code
qr_label = tk.Label(window)
qr_label.pack(pady=10)

# Button to save the QR code
save_button = tk.Button(window, text="Save QR Code", font=("Arial", 14), command=save_qr)
save_button.pack(pady=10)

# Run the main loop
window.mainloop()