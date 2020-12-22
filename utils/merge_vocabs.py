import glob


def write_to_file(corpus, dest_path):
    with open(dest_path, 'w') as f:
        for item in corpus:
            f.write("%s\n" % item)


def create_list_from_file(file_path):
    with open(file_path) as f:
        vocab_list = f.read().splitlines()
    return vocab_list


def list_all_file_path(vocal_dir):
    file_path_list = glob.glob(vocal_dir + '/*')
    print("Number of files: ", len(file_path_list))
    return file_path_list


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


if __name__ == '__main__':
    vocab_dirs = '/home/love_you/ocr-articles/full_vocabs'
    merged_file_path = '/home/love_you/ocr-articles/articles_corpus.txt'
    merge_vocabs(vocab_dirs, merged_file_path)

