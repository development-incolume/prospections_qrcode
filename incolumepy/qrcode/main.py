#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import qrcode
from datagen import funcionariosgen, linksgen
from pathlib import Path
from PIL import Image
from inspect import stack
from random import choices
import datetime as dt


__author__ = "@britodfbr"
funcionariosgen()
linksgen()
output = Path('qrcodes')
output.mkdir(exist_ok=True)
with open('links.json') as f:
    links = json.load(f)
logos = list(Path(__file__).parent.joinpath('..',  'img').resolve().glob('*.png'))


def modo1():
    img_qr = qrcode.make('test')
    img_qr.save(output/'test.png')


def modo2():
    # print(links)
    for name, link in links.items():
        print(name, link)
        imgqr = qrcode.make(link)
        imgqr.save(output/f'{name}.png')


def modo3():
    # taking image which user wants
    # in the QR code center
    Logo_link = Path(__file__).parent / '..'/'img' / 'Logo_incolume.png'
    assert Logo_link.exists(), f"Ops: {Logo_link}"

    logo = Image.open(Logo_link)

    # taking base width
    basewidth = 150

    # adjust image size
    wpercent = (basewidth / float(logo.size[0]))
    hsize = int((float(logo.size[1]) * float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
    QRcode = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )

    # taking url or text
    url = 'https://brito.blog.incolume.com.br/'

    # addingg URL or text to QRcode
    QRcode.add_data(url)

    # generating QR code
    QRcode.make()

    # taking color name from user
    QRcolor = 'Green'

    # adding color to QR code
    QRimg = QRcode.make_image(
        fill_color=QRcolor, back_color="white").convert('RGB')

    # set size of QR code
    pos = ((QRimg.size[0] - logo.size[0]) // 2,
           (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)

    # save the QR code generated
    QRimg.save(output / 'QR.png')

    print('QR code generated!')


def modo4():
    import pyqrcode
    from PIL import Image
    url = pyqrcode.QRCode('http://www.eqxiu.com', error='H')
    url.png('test.png', scale=10)
    im = Image.open('test.png')
    im = im.convert("RGBA")
    logo = Image.open('logo.png')
    box = (135, 135, 235, 235)
    im.crop(box)
    region = logo
    region = region.resize((box[2] - box[0], box[3] - box[1]))
    im.paste(region, box)
    im.show()


def modo5():
    print(logos)
    for name, link in links.items():
        # Path to the Logo in PNG format
        imgfile ,= choices(logos, k=1)
        Logo = Image.open(imgfile)
        # The parameters to set for the image/ QR Code image size, border etc.
        qr = qrcode.QRCode(
            version=12,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=1
        )
        # To add the link to the QR Code
        qr.add_data(link)
        qr.make()
        # You need to convert the image into RGB in order to use it
        img_qr_big = qr.make_image().convert('RGB')

        # Where to place the logo within the QR Code
        pos = ((img_qr_big.size[0] - Logo.size[0]) // 2, (img_qr_big.size[1] - Logo.size[1]) // 2)
        img_qr_big.paste(Logo, pos)
        # Path where you want to save the Generate QR Code along with the name in a series or the number series
        img_qr_big.save(output / f'{stack()[0][3]}-{dt.datetime.now().strftime("%s")}-{name}.png')


if __name__ == '__main__':
    # modo1()
    # modo2()
    # modo3()
    modo5()
