from tag_handler import get_clean_tags


def get_tags_vocab(tags):
    vocab = []
    cleaned_tags = (get_clean_tags(tags))
    for tags in cleaned_tags:
        for tag in tags:
            vocab.append(tag)
    return list(set(vocab))


def get_tags_vocab_as_dict(vocab):
    voc_di = {i: vo for i, vo in enumerate(vocab)}
    voc_di[-1] = 'notags'
    return {vo: int(i) for i, vo in voc_di.items()}
