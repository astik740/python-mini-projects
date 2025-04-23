import qrcode
import image
qr= qrcode.QRCode(
    version= 11,
    box_size=10,
    border=5
)


data="https://www.facebook.com/astik.mandal.12382"
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",back_color="white")
img.save("test.png")
