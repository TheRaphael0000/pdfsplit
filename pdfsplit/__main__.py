#!/usr/bin/env python

import argparse
from .spliter import split, create_pdf


def valid_read_order(o):
    possible = [
        "tblr", "tbrl", "btrl", "btlr",
        "lrtb", "rltb", "rlbt", "lrbt",
    ]

    if o not in possible:
        return False
    return o


def main():
    parser = argparse.ArgumentParser(
        description="Slice every pages of a pdf to a single page in the same PDF")
    parser.add_argument("input", help="Input file")
    parser.add_argument(
        "output", help="Output file (doesn't work with the same as input file)")
    parser.add_argument("-r", "--rows", type=int,
                        default=2, help="Number of rows")
    parser.add_argument("-c", "--cols", type=int,
                        default=2, help="Number of colunms")
    parser.add_argument("-o", "--order", type=valid_read_order,
                        default="tblr", help="Reading order : By default Top-Bottom then Left-Right")

    args = parser.parse_args()
    pages = split(args.input, args.rows, args.cols, args.order)
    pdf = create_pdf(pages)
    pdf.write(open(args.output, "wb"))


if __name__ == "__main__":
    main()
