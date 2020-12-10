from collections import defaultdict
import matplotlib.pyplot as plt
import pandas as pd


def create_list_from_file(file_path):
    with open(file_path) as f:
        vocab_list = f.read().splitlines()
    return vocab_list


def create_num_per_characters_dict(vocal_list):
    character_freq_dict = defaultdict(int)
    for word in vocal_list:
        for character in word:
            character_freq_dict[character] += 1
    return character_freq_dict


def plot_statistics(character_freq_dict):
    character_freq_dict = dict(character_freq_dict)
    fig, ax = plt.subplots(figsize=(12, 9))
    x_range = range(len(character_freq_dict))
    ax.bar(x_range, list(character_freq_dict.values()), color='green', align='center')
    ax.set_xticks(x_range, list(character_freq_dict.keys()), rotation='vertical')
    for index, value in enumerate(list(character_freq_dict.values())):
        ax.text(index, value, value + 10)


def create_dataframe_from_dict(vocal_freq_dict):
    vocal_freq_df = pd.DataFrame.from_dict(vocal_freq_dict)
    return vocal_freq_df


def main():
    vocal_file_path = ''
    corpus_list = create_list_from_file(vocal_file_path)
    vocal_freq_dict = create_num_per_characters_dict(corpus_list)
    plot_statistics(vocal_freq_dict)
