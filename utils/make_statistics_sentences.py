import glob
from collections import defaultdict
import pandas as pd
import matplotlib.pyplot as plt


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


def plot_statistics(character_freq_dict, image_path):
    character_freq_dict = dict(character_freq_dict)
    fig, ax = plt.subplots(figsize=(24, 18))
    x_range = range(len(character_freq_dict))
    ax.bar(x_range, list(character_freq_dict.values()), color='green', align='center')
    ax.set_xticks(x_range, list(character_freq_dict.keys()))
    for index, value in enumerate(list(character_freq_dict.values())):
        ax.text(index, value, str(value + 10))
    plt.savefig(image_path)


def statistics_about_corpus(file_path):
    content = create_list_from_file(file_path)
    num_lines = len(content)
    character_freq_dict = defaultdict(int)
    line_length_dict = defaultdict(int)
    for line in content:
        line_length = len(line)
        line_length_dict[line_length] += 1
        character_set = list(set(line))
        for character in character_set:
            character_freq_dict[character] += 1

    character_freq_df = pd.DataFrame(character_freq_dict.items())
    line_length_df = pd.DataFrame(line_length_dict.items())

    character_freq_df.to_csv('/home/love_you/ocr-articles/character_freq.csv')
    line_length_df.to_csv('/home/love_you/ocr-articles/line_length_freq.csv')
    plot_statistics(character_freq_dict, '/home/love_you/ocr-articles/character_freq.jpeg')
    plot_statistics(line_length_dict, '/home/love_you/ocr-articles/line_length.jpeg')


file_path = '/home/love_you/ocr-articles/merge_vocabs.py'
statistics_about_corpus(file_path)
