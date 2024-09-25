import qrcode
from PIL import Image
data="https://www.linkedin.com/in/swarup-mitra-210473301/"
qr=qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=20,
            border=15,
            )
qr.add_data(data)
qr.make(fit=True)
image=qr.make_image(fill_color="red",back_color="white")
image.save("mylinkdin.png")
