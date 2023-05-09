#!/usr/bin/env python3

import atheris
import sys

with atheris.instrument_imports():
    from pandas import DataFrame as df

def TestOneInput(input):
    fdp = atheris.FuzzedDataProvider(input)
    a = fdp.ConsumeIntInRange(1, 128)
    b = fdp.ConsumeIntInRange(1, 128)
    c = fdp.ConsumeIntInRange(1, 128)

    first = df([[fdp.ConsumeIntInRange(-128, 128) for _ in range(b)] for _ in range(a)])
    second = df([[fdp.ConsumeIntInRange(-128, 128) for _ in range(c)] for _ in range(b)])
    
    first.dot(second)
    first.add(second.T)
    first.sub(second.T)
    first.lt(second.T)
    first.le(second.T)
    first.gt(second.T)
    first.ge(second.T)
    first.ne(second.T)

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
