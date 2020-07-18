"""Usage:
  pyextract [options] <script> <function>...

Options:
  -h, --help  : print this message and exit

Arguments:
  <script>  : path to a `*.py` file
  <function>  : names of functions to print
"""
import importlib
import inspect
import os
from os import path

from argopt import argopt

parser = argopt(__doc__)


def main(argv=None):
    args = parser.parse_args(args=argv)
    os.environ.setdefault("PYTHONPATH", os.curdir)
    mod = importlib.import_module(path.splitext(path.basename(args.script))[0])

    for func in args.function:
        print(inspect.getsource(getattr(mod, func)))


if __name__ == "__main__":
    main()
