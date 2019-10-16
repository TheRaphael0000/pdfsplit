#!/usr/bin/env python

import copy
import sys
from PyPDF2 import PdfFileWriter, PdfFileReader

input = PdfFileReader(open(sys.argv[1], 'rb'))
output = PdfFileWriter()

pages = [input.getPage(i) for i in range(0, input.getNumPages())]

for p in pages:
    a = copy.copy(p)
    b = copy.copy(p)
    c = copy.copy(p)
    d = copy.copy(p)

    (w, h) = p.mediaBox.upperRight

    a.mediaBox.upperLeft = (0, h/2)
    a.mediaBox.lowerRight = (w/2, h)
    output.addPage(a)

    b.mediaBox.upperLeft = (w/2, h/2)
    b.mediaBox.lowerRight = (w, h)
    output.addPage(b)

    c.mediaBox.upperLeft = (0, 0)
    c.mediaBox.lowerRight = (w/2, h/2)
    output.addPage(c)

    d.mediaBox.upperLeft = (w/2, 0)
    d.mediaBox.lowerRight = (w, h/2)
    output.addPage(d)


g = open(sys.argv[2], 'wb')
output.write(g)
