import qrcode
import image 

qr = qrcode.QRCode(
    version = 15,
    box_size = 5,
    border = 5
)

data = "https://www.youtube.com/watch?v=hCoKEbr1pBw"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fit="black",back_color = "white")
img.save("QR Genreted.png")