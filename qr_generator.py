import qrcode

# Function to generate QR Code
def generate_qr(data, filename="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,  # Version of QR code (1 to 40, higher means more data)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR grid
        border=4,  # Border thickness around QR code
    )
    
    qr.add_data(data)  # Adding data to QR code
    qr.make(fit=True)  # Adjusts the QR code to fit data
    
    # Create and save the QR code image
    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"QR Code saved as {filename}")
    img.show()  # Display the QR Code

# Take user input for QR code content
data = input("Enter the data to be encoded in QR Code: ")
generate_qr(data)
