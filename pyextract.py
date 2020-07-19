"""Usage:
  pyextract [options] <script> <function>...

Options:
  -h, --help  : print this message and exit

Arguments:
  <script>  : path to a `*.py` file (use `-` for stdin)
  <function>  : names of functions to print
"""
import importlib
import inspect
import os
from shutil import rmtree
import sys
import tempfile

from argopt import argopt

parser = argopt(__doc__)


def main(argv=None):
    args = parser.parse_args(args=argv)

    tmpdir = None
    try:
        if args.script == "-":
            tmpdir = tempfile.mkdtemp("pyext")
            args.script = os.path.join(tmpdir, "pyext_module.py")
            with open(args.script, "w") as fd:
                fd.write(sys.stdin.read())
            sys.path.insert(0, tmpdir)
        else:
            sys.path.insert(0, os.curdir)

        mod = importlib.import_module(
            os.path.splitext(os.path.basename(args.script))[0]
        )

        for func in args.function:
            print(inspect.getsource(getattr(mod, func)), end="")
    finally:
        if tmpdir:
            rmtree(tmpdir)


if __name__ == "__main__":
    main()
