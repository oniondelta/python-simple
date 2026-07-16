import opencc


class OpenccConverter():

    def run_code(words, json):
        converter = opencc.OpenCC(json)
        words_by_cc = converter.convert(words)
        # print(word_by_cc)
        return words_by_cc


if __name__ == "__main__":
    OpenccConverter()