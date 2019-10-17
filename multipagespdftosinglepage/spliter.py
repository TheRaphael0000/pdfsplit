import copy
from PyPDF2 import PdfFileWriter, PdfFileReader


def split(filename, rows, cols):
    input = PdfFileReader(open(filename, 'rb'))
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

    return output
