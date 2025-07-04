# QR code generation for equipment tracking
import qrcode

def generate_qr(data: str, filename: str):
    img = qrcode.make(data)
    img.save(filename)
    return filename 