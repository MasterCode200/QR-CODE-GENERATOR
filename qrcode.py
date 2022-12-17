import pyqrcode
import png
from pyqrcode import QRCode
s = input("Enter the link to website ")
url = pyqrcode.create(s)
url.svg("YourWebsiteQr.svg",scale=8)#used to convert our website into qr code and save as svg file(file for website).svg file makes the qr code appear on browser as a web page.
url.png("YourWebsiteQr.png",scale=8)#used to convert our website into qr code and save as png file.myqr is file name
