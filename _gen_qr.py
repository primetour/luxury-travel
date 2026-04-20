"""Generate QR codes for the live site URLs."""
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from pathlib import Path

OUT = Path(__file__).parent


def make_qr(url, filename, brand_color=(26, 26, 26)):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=16,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
        color_mask=SolidFillColorMask(
            back_color=(239, 236, 231),      # --bg warm cream
            front_color=brand_color,
        ),
    )
    img.save(OUT / filename)
    print(f'Saved {filename} -> {url}')


if __name__ == '__main__':
    # Landing page
    make_qr('https://primetour.github.io/luxury-travel/', 'qr.png')
    # Direct to Ed07
    make_qr('https://primetour.github.io/luxury-travel/luxury-travel-07/',
            'qr-ed07.png', brand_color=(180, 138, 74))  # --accent
