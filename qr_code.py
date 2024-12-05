import qrcode as qr
# qr is the alias name

# make() used to make a qr_code
img = qr.make("https://lasya1905.github.io/mylittletacoshop/")

# save() used to convert to png format
img.save("mylittletacoshop.png")