from __future__ import absolute_import, division, print_function, unicode_literals

import pandas as pd


def get_cvs_data(path):
    dataframe = pd.read_csv(path)
    return dataframe


def load_tags_and_labels_df(csvpath):
    df = get_cvs_data(csvpath)
    tal = pd.DataFrame(df, columns=['tags', 'category_id'])
    for i, col in enumerate(tal.columns):
        if col == 'tags':
            tal.iloc[:, i] = tal.iloc[:, i].str.replace('"', '')

    return tal
