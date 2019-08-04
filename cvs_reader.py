from __future__ import absolute_import, division, print_function, unicode_literals

import pandas as pd
from sklearn.model_selection import train_test_split

def get_cvs_data(path):
    path = 'data/CAvideos.csv'
    dataframe = pd.read_csv(path)
    dataframe.head()
    return dataframe
