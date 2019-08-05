from __future__ import absolute_import, division, print_function, unicode_literals

# import numpy as np
# import pandas as pd

import tensorflow as tf
# from tensorflow import feature_column
# from tensorflow import keras

from sklearn.model_selection import train_test_split


def df_to_ds(dataframe,target_column, shuffle=True, batch_size=32):
  dataframe = dataframe.copy()
  labels = dataframe.pop(target_column)
  ds = tf.data.Dataset.from_tensor_slices((dict(dataframe), labels))
  if shuffle:
    ds = ds.shuffle(buffer_size=len(dataframe))
  ds = ds.batch(batch_size)
  return ds


def get_tags_as_inputs(tags, batch_size=32):
    train, test = train_test_split(tags, test_size=0.2)
    train, val = train_test_split(train, test_size=0.2)
    print(len(train), 'train examples')
    print(len(val), 'validation examples')
    print(len(test), 'test examples')

    train_ds = df_to_ds(train, target_column='column_id', batch_size=batch_size)
    val_ds = df_to_ds(val, 'column_id', shuffle=False, batch_size=batch_size)
    test_ds = df_to_ds(test, 'column_id', shuffle=False, batch_size=batch_size)

    return train_ds, val_ds, test_ds
