#! /usr/bin/env python3
""" Convert any CSV to a JSONified version. """

import argparse
import csv
import json
import os
import sys


here = os.path.dirname(os.path.abspath(__file__))


def main():
    parser = argparse.ArgumentParser(
        prog='csv2json',
        description='A utility to convert CSVs to JSON quickly and easily.',
        epilog=(
            'If you\'re using csv2json, let me know! '
            'csv2json was built by Brian Schrader.'
        ),
    )
    parser.add_argument(
        '-i',
        '--input',
        type=open,
        default=sys.stdin,
    )
    parser.add_argument(
        '-o','--output',
        type=argparse.FileType('w', encoding='utf-8'),
        default=sys.stdout,
    )
    parser.add_argument(
        '-c',
        '--include-columns',
        nargs='+',
        default=list(),
    )
    parser.add_argument(
        '-x',
        '--exclude-columns',
        nargs='+',
        default=list(),
    )
    parser.add_argument(
        '-p',
        '--pretty',
        action='store_true',
        default=False,
    )
    parser.add_argument(
        '--indent',
        type=int,
        default=4,
    )
    args = parser.parse_args()
    reader = csv.DictReader(args.input)
    json.dump(
        [
            {
                key: val for key, val in row.items()
                if (
                    not args.include_columns
                    or key in args.include_columns
                )
                and key not in args.exclude_columns
            }
            for row in reader
        ],
        args.output,
        indent=(
            args.indent if args.pretty else None
        ),
    )


if __name__ == '__main__':
    main()
