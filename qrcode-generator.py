import qrcode

code = qrcode.make("https://www.google.com")
code.save("qrcode.png")

