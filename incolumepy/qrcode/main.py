#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import qrcode
from datagen import funcionariosgen, linksgen
from pathlib import Path
from PIL import Image

__author__ = "@britodfbr"
funcionariosgen()
linksgen()
output = Path('qrcodes')
output.mkdir(exist_ok=True)


def modo1():
    img_qr = qrcode.make('test')
    img_qr.save(output/'test.png')


def modo2():
    with open('links.json') as f:
        links = json.load(f)
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


if __name__ == '__main__':
    # modo1()
    # modo2()
    modo3()
