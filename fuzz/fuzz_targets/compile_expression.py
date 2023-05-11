#!/usr/bin/env python3

import atheris
import sys
import os

with atheris.instrument_imports():
    from jinja2 import Environment, TemplateSyntaxError

def TestOneInput(input):
    fdp = atheris.FuzzedDataProvider(input)
    try:
        Environment().compile_expression(source=fdp.ConsumeUnicodeNoSurrogates(fdp.ConsumeIntInRange(1, 4096)))
    except TemplateSyntaxError:
        return

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
