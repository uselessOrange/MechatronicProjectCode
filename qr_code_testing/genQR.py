import qrcode

# Create a QR code instance with some data
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data("1")
qr.make(fit=True)

# Generate an image of the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save("qrcode.png")
