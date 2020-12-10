from .make_statistics_num_per_characters import create_list_from_file
from .create_vietnamese_corpus import list_all_file_path
from .create_vietnamese_corpus import write_to_file


def merge_vocabs(vocab_dirs, merged_file_path):
    vocab_path_list = list_all_file_path(vocab_dirs)
    merged_corpus = []
    for vocab_path in vocab_path_list:
        vocal_character_list = create_list_from_file(vocab_path)
        merged_corpus.extend(vocal_character_list)
    print("Before merge: ", len(merged_corpus))
    merged_corpus = list(set(merged_corpus))
    print("After merge: ", len(merged_corpus))
    write_to_file(merged_corpus, merged_file_path)
