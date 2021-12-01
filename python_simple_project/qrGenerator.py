import png
import pyqrcode

def qrcode():
    #you can input text / number / url website
    inputSomething = pyqrcode.create(input())
    #make the inputurl to png and save with the file named "qrcode.png"
    inputSomething.png('qrcodepython.png', scale=6)
    print('QR generated')

if __name__ == '__main__':
    qrcode()