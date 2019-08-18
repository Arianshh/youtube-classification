from __future__ import absolute_import, division, print_function, unicode_literals

import pandas as pd


def get_cvs_data(path):
    dataframe = pd.read_csv(path, error_bad_lines=False)
    return dataframe


def load_dataframe(csvpath, columns):
    csvdf = get_cvs_data(csvpath)
    df = pd.DataFrame(csvdf, columns=columns)
    for i, col in enumerate(df.columns):
        if col == 'tags':
            df.iloc[:, i] = (df.iloc[:, i]).str.replace('"', '')

    return df
