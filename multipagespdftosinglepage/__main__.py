#!/usr/bin/env python

import argparse
from .spliter import split


def main():
    parser = argparse.ArgumentParser(
        description="Slice every pages of a pdf to a single page in the same PDF")
    parser.add_argument("input", help="Input file")
    parser.add_argument(
        "output", help="Output file (doesn't work with the same as input file)")
    parser.add_argument('-r', '--rows', type=int,
                        default=2, help="Number of rows")
    parser.add_argument('-c', '--cols', type=int,
                        default=2, help="Number of colunms")

    args = parser.parse_args()
    pdf = split(args.input, args.rows, args.cols)
    pdf.write(open(args.output, 'wb'))


if __name__ == '__main__':
    main()
