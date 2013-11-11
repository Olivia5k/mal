#!/usr/bin/env python
# coding: utf-8

"""
mal

Usage:
  mal issues
  mal issues <issue>

"""


from docopt import docopt


def main():
    args = docopt(__doc__)
    print(args)


if __name__ == "__main__":
    main()
