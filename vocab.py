from tag_handler import get_clean_tags


def get_tags_vocab(frequency_dict, threshold):
    for tag, freq in frequency_dict.items():
        if freq < threshold:
            del frequency_dict[tag]

    return frequency_dict


def get_tags_vocab_as_dict(pruned_vocab):
    vocab = []
    for tag in pruned_vocab.keys():
        vocab.append(tag)

    voc_di = {i: vo for i, vo in enumerate(vocab)}
    voc_di[-1] = 'notags'
    return {vo: int(i) for i, vo in voc_di.items()}


def get_tags_frequency(tags):
    frequency_dict = {}
    cleaned_tags = get_clean_tags(tags)
    for tags in cleaned_tags:
        for tag in tags:
            if not frequency_dict[tag]:
                frequency_dict[tag] = 0
                continue
            frequency_dict[tag] = 1

    return frequency_dict
