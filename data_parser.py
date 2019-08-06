import json

import pandas as pd

import cvs_reader


def get_category_title_dict(json_path):
    dict = {}
    with open(json_path) as json_file:
        data = json.load(json_file)
        for item in data['items']:
            dict.update({item['id']: item['snippet']['title']})

    return dict


def get_tags_and_labels(csvpath):
    df = cvs_reader.get_cvs_data(csvpath)
    tal = pd.DataFrame(df, columns=['tags', 'category_id'])
    for i, col in enumerate(tal.columns):
        if col == 'tags':
            tal.iloc[:, i] = tal.iloc[:, i].str.replace('"', '')
            tal.iloc[:, i] = tal.iloc[:, i].str.replace('|', '.')

    return tal


def get_tags(csvpath):
    return cvs_reader.get_cvs_data(csvpath)['tags']


def get_clean_tags(tags):
    normalized_tags = []
    final_tags = []
    i = 0

    for tag in tags:
        normalized_tags.append(tag.split("|"))
        final_tags.append([])
    for tag in normalized_tags:
        for word in tag:
            if '"' in word:
                word = word.replace('"', '')
            final_tags[i].append(word)
    return final_tags


def get_labels(csvpath):
    return cvs_reader.get_cvs_data(csvpath)['category_id']


def get_vocab(tags):
    vocab = set(list(get_clean_tags(tags)))
    return vocab
