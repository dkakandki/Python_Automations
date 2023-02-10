import qrcode
data = 'https://github.com/dkakandki'
qr = qrcode.QRCode(
    version = 1,
    border = 10,
    box_size = 15
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color = 'yellow', back_color = 'black')
img.save('QRcode.jpg')