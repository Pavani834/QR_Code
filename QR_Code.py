import qrcode
website_link = 'https://www.linkedin.com/in/pavanikalyani/'
qr = qrcode.QRCode(
    version=1,
    box_size=5,
    border=5
)
qr.add_data(website_link)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save('LinkedIn_qr.png')
