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


def load_tags_and_labels_df(csvpath):
    df = cvs_reader.get_cvs_data(csvpath)
    tal = pd.DataFrame(df, columns=['tags', 'category_id'])
    for i, col in enumerate(tal.columns):
        if col == 'tags':
            tal.iloc[:, i] = tal.iloc[:, i].str.replace('"', '')

    return tal


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
        i += 1
    return final_tags


def get_vocab(tags):
    vocab = []
    cleaned_tags = (get_clean_tags(tags))
    for tags in cleaned_tags:
        for tag in tags:
            vocab.append(tag)
    return list(set(vocab))


def get_vocab_as_dict(vocab):
    voc_di = {i: vo for i, vo in enumerate(vocab)}
    voc_di[0] = 'notags'
    return {vo: i for i, vo in voc_di.items()}


def remove_infrequent_values(threshold, dirty_tags):
    clean_tags = get_clean_tags(dirty_tags)
    union = []
    for index in range(0, len(clean_tags)):
        union += clean_tags[index] + ['SEP']
    for tag in union:
        if tag != 'SEP' and union.count(tag) <= threshold:
            union.pop(tag)

    return union[0].split('SEP')
