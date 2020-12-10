from .make_statistics_num_per_characters import create_list_from_file
from .create_vietnamese_corpus import list_all_file_path
from .create_vietnamese_corpus import write_to_file


def create_title_vocab(vocab):
    title_vocab = []
    for word in vocab:
        title_vocab.append(word.title())
    return title_vocab


def create_uppercase_vocab(vocab):
    upper_vocab = []
    for word in vocab:
        upper_vocab.append(word.upper())
    return upper_vocab


def create_lowercase_vocab(vocab):
    lower_vocab = []
    for word in vocab:
        lower_vocab.append(word.lower())
    return lower_vocab


def augment_data_vocab(vocab_file_path, dest_file_path):
    vocab = create_list_from_file(vocab_file_path)
    upper_vocab = create_uppercase_vocab(vocab)
    vocab.extend(upper_vocab)
    title_vocab = create_title_vocab(vocab)
    vocab.extend(title_vocab)
    lower_vocab = create_lowercase_vocab(vocab)
    vocab.extend(lower_vocab)
    print("Length before merge: ", len(vocab))
    vocab = set(vocab)
    print("Length after merge: ", len(vocab))
    write_to_file(vocab, dest_file_path)
