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

    center = (w / 2, h / 2)

    a.mediaBox.upperLeft = (0, 0)
    a.mediaBox.lowerRight = center

    b.mediaBox.upperRight = (w, 0)
    b.mediaBox.lowerLeft = center

    c.mediaBox.lowerLeft = (0, h)
    c.mediaBox.upperRight = center

    d.mediaBox.upperLeft = center
    d.mediaBox.lowerRight = (w, h)

    output.addPage(a)
    output.addPage(b)
    output.addPage(c)
    output.addPage(d)

g = open(sys.argv[2], 'wb')
output.write(g)
