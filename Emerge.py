#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: Emerge.py
# Created Time: 3/26/2019 16:40:38
#########################################################################

import sys
from PIL import Image as im

class Fmerge:
    @staticmethod
    def default(a, b):
        a /= 255
        b /= 255
        alpha = 1 - (Fmerge.c_e * a + (b - 1) * Fmerge.d_e) / Fmerge.c_d
        if alpha != 0:
            color = Fmerge.d + (Fmerge.d_e * Fmerge.c_d * b) / ((a - 1) * Fmerge.c_e + Fmerge.d_e * b)
            color = int(color * 255)
        else:
            color = 0
        alpha = int(alpha * 255)
        return (color, alpha)

    @staticmethod
    def init(cls, inc=1, ind=0, ine=1/2):
        Fmerge.c = inc
        Fmerge.d = ind
        Fmerge.e = ine
        Fmerge.c_d = inc - ind
        Fmerge.c_e = inc - ine
        Fmerge.d_e = ind - ine

    c = 1
    d = 0
    e = 1/2
    c_d = 1
    c_e = 1/2
    d_e = -1/2

class Emerger:
    def __init__(self, img1, img2):
        self.size = (
                max(img1.size[0], img2.size[1]),
                max(img1.size[0], img2.size[1])
                )
        self.img = []
        self.img.append(img1)
        self.img.append(img2)

    def resize(self, mode='stretch'):
        if mode == 'stretch':
            self.img[0] = self.img[0].resize(self.size, resample=im.LANCZOS)
            self.img[1] = self.img[1].resize(self.size, resample=im.LANCZOS)
        return

    def emerge(self, mode='default'):
        if mode == 'default':
            if not self.samesize():
                print('Images must have the same size! Use resize() method!')
                return
            datain1 = list(self.img[0].convert(mode='L').getdata())
            datain2 = list(self.img[1].convert(mode='L').getdata())
            dataout = []
            for i in range(len(datain1)):
                dataout.append(Fmerge.default(datain1[i], datain2[i]))
            self.out = im.new('LA', self.size)
            self.out.putdata(dataout)
            self.out = self.out.convert(mode='RGBA')
        return

    def output(self, outfilename):
        if self.out:
            self.out.save(outfilename)
        else:
            print("No output image. Use emerge() method!")

    def samesize(self):
        return self.img[0].size == self.img[1].size

def main(argv):
    em = Emerger(im.open(argv['fname1']), im.open(argv['fname2']))
    em.resize()
    em.emerge()
    em.output(argv['outfname'])

if __name__ == '__main__':
    opts = {}
    args = ['this', 'fname1', 'fname2', 'outfname']
    i = 0
    try:
        for arg in sys.argv:
            if arg[0] == '-':
                opts[arg] = i
            else:
                opts[args[i]] = arg
                i += 1
    except:
        print(
                """
Usage:

	python emerge.py [img1 [img2='b.png' [outimg='out.png']]]
    """)
    finally:
        main(opts)
