from kivy.app import App
# from kivy.lang import Builder
# from kivy_garden.zbarcam import ZBarCam
from kivy.core.window import Window
from qrcod import read_barcodes
import cv2
from pyzbar import pyzbar

Window.size = (400, 700)

class QrCode(App):
    def build(self):
        camera = cv2.VideoCapture(0)
        ret, frame = camera.read()
        while ret:
            ret, frame = camera.read()
            frame,qr_text = read_barcodes(frame)
            if qr_text:
                return qr_text
            cv2.imshow('Barcode/QR code reader', frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break


QrCode().run()
