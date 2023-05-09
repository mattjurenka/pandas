#!/usr/bin/env python3

import atheris
import sys

with atheris.instrument_imports():
    from pandas import Series

def TestOneInput(input):
    fdp = atheris.FuzzedDataProvider(input)
    length = fdp.ConsumeIntInRange(1, 128)

    series = Series([fdp.ConsumeIntInRange(-128, 128) for _ in range(length)])

    series.std()
    series.mean()
    series.var()
    series.kurtosis()


def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
