from underthesea import sent_tokenize


def create_list_from_file(file_path):
    with open(file_path) as f:
        paragraph_list = f.read().splitlines()
    return paragraph_list


def segment_paragraphs(paragraph_list):
    sentences_list = []
    count = 1
    for paragraph in paragraph_list:
        sentences_list.extend(sent_tokenize(paragraph))
        print(f'{count}', end='\t')
        count = count + 1
    return sentences_list


def write_to_file(corpus, dest_path):
    with open(dest_path, 'w') as f:
        for item in corpus:
            f.write("%s\n" % item)


def find_all_txt_file(src_dir):
    from pathlib import Path
    text_path_list = list(Path(src_dir).rglob("*.[tT][xX][tT]"))
    text_path_list = [str(text_path) for text_path in text_path_list]
    return text_path_list


def copy_file(text_path_list, dest_dir):
    import shutil
    for text_path in text_path_list:
        shutil.copy2(text_path_list, dest_dir)


def concatenate_files(src_dir, dest_file_path):
    import glob
    file_path_list = glob.glob(src_dir + '/*.[tT][xX][tT]')
    contents = []
    for file_path in file_path_list:
        with open(file_path, 'r') as f:
            contents.extend(f.read())
    contents_str = '\n'.join(contents)
    with open(dest_file_path, 'w') as f:
        f.write(contents_str)


def main():
    corpus_path = '/home/love_you/ocr-articles/vietnamese_text.txt'
    dest_path = '/home/love_you/ocr-articles/sentences_from_vietnamese_text.txt'
    paragraph_list = create_list_from_file(corpus_path)
    sentence_list = segment_paragraphs(paragraph_list)
    print("Number of sentences: ", len(sentence_list))
    write_to_file(sentence_list, dest_path)
    # 637556 sentences kaggle corpus
    # corpus_path = '/content/train_news'
    # dest_path = '/content/sentences_from_vntc.txt'
    # import glob
    # text_path_list = glob.glob(corpus_path + '/*.txt')
    # corpus = []
    # for text_path in text_path_list:
    #     paragraph_list = create_list_from_file(text_path)
    #     sentence_list = segment_paragraphs(paragraph_list)
    #     corpus.extend(sentence_list)
    # write_to_file(sentence_list, dest_path)

main()
