"""Answers to exercises in Think Stats, started from a copy of nsfg.py."""

from __future__ import print_function

from collections import defaultdict
import numpy as np
import sys

import thinkstats2


def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz'):
    """Reads the NSFG pregnancy data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    # CleanFemPreg(df)
    return df

if __name__ == '__main__':
    df = ReadFemResp()
    print(df.pregnum.value_counts().sort_index())
