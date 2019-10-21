import copy
from PyPDF2 import PdfFileWriter, PdfFileReader


def order_to_index(rows, cols, order):
    swap_xy = "l" == order[0] or "l" == order[1]
    if swap_xy:
        x = order[0:2]
        y = order[2:4]
    else:
        x = order[2:4]
        y = order[0:2]
    x_order = 1 if x[0] == "l" else -1
    y_order = 1 if y[0] == "t" else -1
    return swap_xy, x_order, y_order


def create_pdf(pages):
    output = PdfFileWriter()
    for page in pages:
        output.addPage(page)
    return output


def split(filename, rows, cols, order):
    input = PdfFileReader(open(filename, "rb"))
    pages = []

    swap_xy, x_order, y_order = order_to_index(rows, cols, order)

    def crop_add_page(subpage_i, subpage_j):
        x = subpage_i * col_w
        y = subpage_j * row_h
        page_copy = copy.copy(page)
        page_copy.mediaBox = copy.copy(page_copy.mediaBox)

        ll = (x, y)
        page_copy.mediaBox.setLowerLeft(ll)
        ur = (x+col_w, y+row_h)
        page_copy.mediaBox.setUpperRight(ur)

        pages.append(page_copy)

    for page_i in range(input.getNumPages()):
        page = input.getPage(page_i)
        (w, h) = page.mediaBox.upperRight

        col_w = w/cols
        row_h = h/rows

        if swap_xy:
            for subpage_i in range(rows)[::x_order]:
                for subpage_j in range(cols)[::-y_order]:
                    crop_add_page(subpage_i, subpage_j)
        else:
            for subpage_j in range(cols)[::-y_order]:
                for subpage_i in range(rows)[::x_order]:
                    crop_add_page(subpage_i, subpage_j)

    return pages
