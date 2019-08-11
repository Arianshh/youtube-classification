from __future__ import absolute_import, division, print_function, unicode_literals

import pandas as pd


def get_cvs_data(path):
    dataframe = pd.read_csv(path)
    dataframe.head()
    return dataframe
