"""Writes a message to a file.

Usage:
  foo [options]

Options:
  -o OUT, --output OUT  : output file name (default: stdout)
  --bar  : write `bar` instead of `foo`
"""
import sys
from argopt import argopt

parser = argopt(__doc__)


def foo(fd):
    fd.write("I'm a foo\n")


def bar(fd):
    fd.write("I'm a bar\n")


def main(argv=None):
    args = parser.parse_args(args=argv)
    if args.output:
        out = open(args.output, "w")
    else:
        out = sys.stdout
    if args.bar:
        bar(out)
    else:
        foo(out)
    if args.output:
        out.close()


if __name__ == "__main__":
    main()
