import json

class unicode_to_character():
    with open("input_unicode.txt",mode="r",encoding="utf-8") as infile:
        unicodeword=infile.read()

        # unicodeword = unicodeword.replace('\n', '\\n')
        unicodeword = unicodeword.replace('\\\\', '\\')
        # unicodeword = eval(unicodeword)

        # print(unicodeword)
        # print(unicodeword.encode('utf-8').decode("unicode_escape"))
        to_be_character = unicodeword.encode('utf-8').decode("unicode_escape")

    with open("out_character.txt",mode="w",encoding="utf-8") as outfile:
        outfile.write(to_be_character)

    # s="\\u9F9E\\uBCC4"
    # print(json.loads(f'"{s}"'))


if __name__ == "__main__":
    unicode_to_character()