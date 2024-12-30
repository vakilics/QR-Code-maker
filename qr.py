#requres: qrcode and pillow library
import qrcode
image1 = qrcode.make("http://127.0.0.1:8000")
image1.save("qr.png")

image2 = qrcode.make("https://www.linkedin.com/in/abdul-rahman-vakili-052172120")
image2.save("vakili-linkedin.png")

