import copy
import itertools

import numpy as np
from PyPDF2 import PdfFileWriter, PdfFileReader


def create_pdf(pages):
    output = PdfFileWriter()
    for page in pages:
        output.addPage(page)
    return output


def split(filename, rows, cols, xflip, yflip, transpose):
    input = PdfFileReader(open(filename, "rb"), strict=False)

    pages = []

    order = np.arange(rows * cols)

    if transpose:
        order = order.reshape((cols, rows))
        order = order.T
    else:
        order = order.reshape((rows, cols))

    if xflip:
        order = order[::, ::-1]
    if yflip:
        order = order[::-1, ::]

    print("Reading order of the sub pages : ")
    print(order)
    order = order.flatten()
    print(order)

    for page_i in range(input.getNumPages()):
        page = input.getPage(page_i)
        (w, h) = page.mediaBox.upperRight
        col_w = w / cols
        row_h = h / rows

        sub_pages = []
        for r, c in itertools.product(range(rows), range(cols)):
            # inverse v-axis because the origin is bottom left
            r_pos = (rows - r - 1) * row_h
            c_pos = c * col_w

            sub_page = copy.copy(page)
            sub_page.mediaBox = copy.copy(sub_page.mediaBox)
            sub_page.mediaBox.setLowerLeft((c_pos, r_pos))
            sub_page.mediaBox.setUpperRight((c_pos + col_w, r_pos + row_h))

            sub_pages.append(sub_page)

        sub_pages = [sub_pages[i] for i in order]

        pages.extend(sub_pages)

    return pages
