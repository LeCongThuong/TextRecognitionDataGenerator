from underthesea import word_tokenize
import glob
import re
import os
import multiprocessing


def read_from_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    return content


def write_to_file(corpus, dest_path):
    with open(dest_path, 'w') as f:
        for item in corpus:
            f.write("%s\n" % item)


def segment_string(file_path):
    seg_content = []
    space_content = []
    with open(file_path) as f:
        content = f.read().splitlines()
    for line in content:
        segment_line = word_tokenize(line)
        space_line = line.split()
        seg_content.extend(segment_line)
        space_content.extend(space_line)
    return seg_content, space_content


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


def create_vocab(file_path_dict):
    character_vocab = 'hjbóẺoÝLvÚẼÁÂẩởĨỈtgKứẾmŨÒWsăỷịơIÔỀửãùaXP9ẰẳỉẹỶzầẪâỸỎảệyOựỬẵỘxCỐlỲD6ộỦỒĂƠÌồ1áTFnỆpHẽờếỏẢYẨUắƯẦíÃẤJèýẲ2i4ẬỊÊÓớR7ÙÕàGỨềỳecêSéừqQạòấỮ0ốẫ5õfỗđỡúNũỤợỖỠMằẸôỚặuỌỞụÀEkĐÉBưẮ3ỂễAìỜủỔỢổọwậdZĩẻ8ỄỰểrÈẴÍỪẶẠữỹV '
    # vocab_dir = '/home/love_you/ocr-articles/articles'

    # file_path_list = list_all_file_path(vocab_dir)
    # count = 1
    saved_file_dir = '/home/love_you/ocr-articles/add_result'
    for index, file_path in file_path_dict.items():
        seg_content, space_content = segment_string(file_path)
        print("Done segment_list")
        filtered_segment_list = filter_characters(seg_content, character_vocab)
        filtered_space_list = filter_characters(space_content, character_vocab)
        del seg_content
        del space_content
        print("Length before removing duplications: ", len(filtered_segment_list))
        print("Length space before removing duplications: ", len(filtered_space_list))
        seg_corpus = set(filtered_segment_list)
        space_corpus = set(filtered_space_list)
        del filtered_segment_list
        del filtered_space_list
        print("Length after removing duplications: ", len(seg_corpus))
        print("Length space after removing duplications: ", len(space_corpus))
        seg_saved_file_path = saved_file_dir + os.path.sep + f'add_seg_{str(index)}.txt'
        space_saved_file_path = saved_file_dir + os.path.sep + f'add_space_{str(index)}.txt'

        write_to_file(seg_corpus, seg_saved_file_path)
        write_to_file(space_corpus, space_saved_file_path)
        print(file_path)
        # print(count)
        # count = count + 1
        del seg_corpus
        del space_corpus


def get_dict_from_list(start_index_list, index, file_path_dict, is_last=False):
    if is_last:
        index_list = list(range(start_index_list[index], len(file_path_dict)))
    else:
        index_list = list(range(start_index_list[index], start_index_list[index + 1]))
    result_dict = {}
    for position in index_list:
        result_dict[position] = file_path_dict[position]
    return result_dict


def main():
    vocab_dir = '/home/love_you/ocr-articles/add_vocab'
    file_path_list = list_all_file_path(vocab_dir)
    index_range = list(range(len(file_path_list)))
    file_path_dict = dict(zip(index_range, file_path_list))
    create_vocab(file_path_dict)
    # num_thread = 8
    # index_distance = len(file_path_dict) // num_thread
    # start_index_list = [i * index_distance for i in range(num_thread)]
    #
    # t0 = multiprocessing.Process(target=create_vocab, args=(get_dict_from_list(start_index_list, 0, file_path_dict),))
    # t1 = multiprocessing.Process(target=create_vocab, args=(get_dict_from_list(start_index_list, 1, file_path_dict),))
    # t2 = multiprocessing.Process(target=create_vocab, args=(get_dict_from_list(start_index_list, 2, file_path_dict),))
    # t3 = multiprocessing.Process(target=create_vocab, args=(get_dict_from_list(start_index_list, 3, file_path_dict),))
    # t4 = multiprocessing.Process(target=create_vocab, args=(get_dict_from_list(start_index_list, 4, file_path_dict),))
    # t5 = multiprocessing.Process(target=create_vocab, args=(get_dict_from_list(start_index_list, 5, file_path_dict),))
    # t6 = multiprocessing.Process(target=create_vocab, args=(get_dict_from_list(start_index_list, 6, file_path_dict),))
    # t7 = multiprocessing.Process(target=create_vocab, args=(get_dict_from_list(start_index_list, 7, file_path_dict, True),))
    #
    # t0.start()
    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()
    # t5.start()
    # t6.start()
    # t7.start()
    #
    # t0.join()
    # t1.join()
    # t2.join()
    # t3.join()
    # t4.join()
    # t5.join()
    # t6.join()
    # t7.join()

    print("The end!")


if __name__ == '__main__':
    main()



