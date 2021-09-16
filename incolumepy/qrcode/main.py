#!/usr/bin/env python
# -*- coding: utf-8 -*-
import qrcode
from datagen import funcionariosgen, linksgen
from pathlib import Path
import json


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


if __name__ == '__main__':
    # modo1()
    modo2()
