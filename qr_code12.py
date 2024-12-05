import qrcode
from PIL import Image
import qrcode.constants

# QRCode() allows you to customize the qrcode before encoding data into it
qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,
                   border=4,
                   )
#ERROR_CORRECT_H - error correction level 
#box_size=10 - size of each box in QR Grid
#border=4 - Thickness of the border(min is 4)

qr.add_data("https://lasya1905.github.io/mylittletacoshop/")

qr.make(fit=True)
img = qr.make_image(fill_color="blue", back_color="white")

img.save("taco_shop_qr.png")