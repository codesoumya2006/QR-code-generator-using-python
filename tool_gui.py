import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def generate_qr():
    data = entry.get()
    if not data:
        messagebox.showerror("Error", "Please enter data to generate QR Code")
        return
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    
    img.thumbnail((200, 200))  # Resize for display
    img_tk = ImageTk.PhotoImage(img)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk
    qr_label.qr_image = img  # Store the original image

def save_qr():
    if not hasattr(qr_label, 'qr_image'):
        messagebox.showerror("Error", "No QR Code to save. Generate one first!")
        return
    
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All Files", "*.*")])
    if file_path:
        qr_label.qr_image.save(file_path)
        messagebox.showinfo("Success", f"QR Code saved as {file_path}")

# GUI Setup
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x500")
root.resizable(False, False)

tk.Label(root, text="Enter data for QR Code:").pack(pady=10)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=10)

qr_label = tk.Label(root)
qr_label.pack()

save_button = tk.Button(root, text="Save QR Code", command=save_qr)
save_button.pack(pady=10)

root.mainloop()
