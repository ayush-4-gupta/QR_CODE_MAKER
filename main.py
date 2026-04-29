import qrcode

# give whatever you want to make qr

redirect_to=input("enter your data  : ")

qr=qrcode.make(redirect_to)

# saving the qr with your name
qr.save("QR_name")

qr.show()
