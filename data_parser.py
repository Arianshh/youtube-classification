import json

def get_category_tite_dict(json_path):
    dict = {}
    with open(json_path) as json_file:
        data = json.load(json_file)
        for item in data['items']:
            dict.update({item['id']:item['snippet']['title']})

    return dict
