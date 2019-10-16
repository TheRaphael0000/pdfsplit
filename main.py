#!/usr/bin/env python

import copy
import sys
from PyPDF2 import PdfFileWriter, PdfFileReader


rows = 2
cols = 2

input = PdfFileReader(open(sys.argv[1], 'rb'))
output = PdfFileWriter()

for page_i in range(input.getNumPages()):
    page = input.getPage(page_i)
    (w, h) = page.mediaBox.upperRight

    col_w = w/cols
    row_h = h/rows

    for subpage_i in range(rows):
        x = subpage_i * col_w
        for subpage_j in range(cols)[::-1]:
            y = subpage_j * row_h
            c = copy.copy(page)
            c.mediaBox = copy.copy(c.mediaBox)

            ll = (x, y)
            c.mediaBox.setLowerLeft(ll)
            ur = (x+col_w, y+row_h)
            c.mediaBox.setUpperRight(ur)

            output.addPage(c)

output.write(open(sys.argv[2], 'wb'))
