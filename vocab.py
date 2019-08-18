from tag_handler import get_clean_tags


def get_tags_vocab(frequency_dict, threshold):
    pruned_vocab = []
    for tag, freq in frequency_dict.items():
        if freq > threshold:
            pruned_vocab += [tag]

    return pruned_vocab


def get_tags_vocab_as_dict(pruned_vocab):

    voc_di = {i: vo for i, vo in enumerate(pruned_vocab)}
    voc_di[-1] = 'notags'
    return {vo: int(i) for i, vo in voc_di.items()}


def get_tags_frequency(tags):
    frequency_dict = {}
    cleaned_tags = get_clean_tags(tags)
    for tags in cleaned_tags:
        for tag in tags:
            if tag not in frequency_dict:
                frequency_dict[tag] = 0
                continue
            frequency_dict[tag] += 1

    return frequency_dict
