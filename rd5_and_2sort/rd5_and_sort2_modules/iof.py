import re


class IOfile():
    # def __init__(self,file_name):
    #     self.name=file_name
    # def input_file(self):
    #     with open(self.name,mode="r",encoding="utf-8") as infile:
    #         words=infile.read()
    #     return words
    # def output_file(self.name,words):
    #     with open(name,mode="w",encoding="utf-8") as outfile:
    #         outfile.write(words)

    def input_file(name):
        with open(name,mode="r",encoding="utf-8") as infile:
            words=infile.read()
        return words

    def output_file(name,words):
        with open(name,mode="w",encoding="utf-8") as outfile:
            outfile.write(words)


if __name__ == "__main__":
    IOfile()