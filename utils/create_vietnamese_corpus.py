from underthesea import word_tokenize
import glob
import re


def read_from_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    return content


def write_to_file(corpus, dest_path):
    with open(dest_path, 'w') as f:
        for item in corpus:
            f.write("%s\n" % item)


def segment_string(content):
    return word_tokenize(content)


def list_all_file_path(vocal_dir):
    file_path_list = glob.glob(vocal_dir + '/*')
    print("Number of files: ", len(file_path_list))
    return file_path_list


def filter_characters(segment_list, vocab_character):
    out_of_char = f'[^{vocab_character}]'
    filtered_segment_list = []
    for segment_word in segment_list:
        if re.search(out_of_char, segment_word):
            continue
        filtered_segment_list.append(segment_word)
    return filtered_segment_list


def main():
    character_vocab = '0123456789aAàÀảẢãÃáÁạẠăĂằẰẳẲẵẴắẮặẶâÂầẦẩẨẫẪấẤậẬbBcCdDđĐeEèÈẻẺẽẼéÉẹẸêÊềỀểỂễỄếẾệỆfFgGhHiIìÌỉỈĩĨíÍịỊjJkKlLmMnNoO '
    vocab_dir = ''
    saved_file_path = ''
    file_path_list = list_all_file_path(vocab_dir)
    corpus = []
    count = 1
    for file_path in file_path_list:
        content = read_from_file(file_path)
        segment_list = segment_string(content)
        filtered_segment_list = filter_characters(segment_list, character_vocab)
        corpus.append(filtered_segment_list)
        print(count)
        count = count + 1
    print("Length before removing duplications: ", len(corpus))
    corpus = set(corpus)
    print("Length after removing duplications: ", len(corpus))
    write_to_file(corpus, saved_file_path)
