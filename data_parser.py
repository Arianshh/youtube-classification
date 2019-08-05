import json
import cvs_reader
from pandas import pd


def get_category_title_dict(json_path):
    dict = {}
    with open(json_path) as json_file:
        data = json.load(json_file)
        for item in data['items']:
            dict.update({item['id']: item['snippet']['title']})

    return dict


def get_tags_and_labels(csvpath):
    df = cvs_reader.get_cvs_data('data/CAvideos.csv')
    tal = pd.DataFrame(df, columns=['tags', 'category_id'])

    return tal


def get_tags(csvpath):
    return cvs_reader.get_cvs_data(csvpath)['tags']


def get_labels(csvpath):
    return cvs_reader.get_cvs_data(csvpath)['category_id']


def get_vocab(tags):
    splited_tags = []
    for tag in tags:
        splited_tags += tag.split("|")
    for tag in splited_tags:
        tag = tag[1:len(tag) - 1]

        return list(set((splited_tags)))
