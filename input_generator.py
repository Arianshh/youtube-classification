from data_parser import get_vocab


def get_tags_as_inputs(tags):
    vocab = get_vocab(tags)
    encoded_input = []
    for tag in tags:
        encoded_input.append(vocab[tag])
