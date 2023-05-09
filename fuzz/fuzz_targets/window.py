#!/usr/bin/env python3

import atheris
import sys

with atheris.instrument_imports():
    from pandas import Series, DataFrame

def TestOneInput(input):
    fdp = atheris.FuzzedDataProvider(input)
    length = fdp.ConsumeIntInRange(1, 128)

    series = Series([fdp.ConsumeIntInRange(-128, 128) for _ in range(length)])
    df = DataFrame([fdp.ConsumeIntInRange(-128, 128) for _ in range(length)] for _ in range(3))
    
    series.rolling(fdp.ConsumeIntInRange(1, 10)).count()
    df.rolling(fdp.ConsumeIntInRange(1, 10)).count()

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
