import cv2
from pyzbar import pyzbar

def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    qr_text = ''
    cv2.rectangle(frame, (232, 181),(232+220, 181+220), (0, 255, 0), 2)
    for barcode in barcodes:
        qr_text = barcode.data.decode('utf-8')
    if qr_text:
        print(qr_text)
        return frame,qr_text
    else:
        return frame,''

def main():
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

if __name__ == '__main__':
    main()
