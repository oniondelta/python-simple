import re


class Pinyin2Pinyin():
    # def __init__(self,input,output):
    #     self.input=input
    #     self.output=output
    # def run_code(self):
    #     with open(self.input,mode="r",encoding="utf-8") as infile:
    #         word=infile.read()

    def run_code(words):

        wc=re.sub(r"([a-zü]*)ī([a-zü]*)",r"\1i\2@",words)
        wc=re.sub(r"([a-zü]*)ū([a-zü]*)",r"\1u\2@",wc)
        wc=re.sub(r"([a-zü]*)ē([a-zü]*)",r"\1e\2@",wc)
        wc=re.sub(r"([a-zü]*)ō([a-zü]*)",r"\1o\2@",wc)
        wc=re.sub(r"([a-zü]*)ā([a-zü]*)",r"\1a\2@",wc)

        wc=re.sub(r"([a-zü]*)í([a-zü]*)",r"\1i\2@@",wc)
        wc=re.sub(r"([a-zü]*)ú([a-zü]*)",r"\1u\2@@",wc)
        wc=re.sub(r"([a-zü]*)é([a-zü]*)",r"\1e\2@@",wc)
        wc=re.sub(r"([a-zü]*)ó([a-zü]*)",r"\1o\2@@",wc)
        wc=re.sub(r"([a-zü]*)á([a-zü]*)",r"\1a\2@@",wc)

        wc=re.sub(r"([a-zü]*)ǐ([a-zü]*)",r"\1i\2@@@",wc)
        wc=re.sub(r"([a-zü]*)ǔ([a-zü]*)",r"\1u\2@@@",wc)
        wc=re.sub(r"([a-zü]*)ě([a-zü]*)",r"\1e\2@@@",wc)
        wc=re.sub(r"([a-zü]*)ǒ([a-zü]*)",r"\1o\2@@@",wc)
        wc=re.sub(r"([a-zü]*)ǎ([a-zü]*)",r"\1a\2@@@",wc)

        wc=re.sub(r"([a-zü]*)ì([a-zü]*)",r"\1i\2@@@@",wc)
        wc=re.sub(r"([a-zü]*)ù([a-zü]*)",r"\1u\2@@@@",wc)
        wc=re.sub(r"([a-zü]*)è([a-zü]*)",r"\1e\2@@@@",wc)
        wc=re.sub(r"([a-zü]*)ò([a-zü]*)",r"\1o\2@@@@",wc)
        wc=re.sub(r"([a-zü]*)à([a-zü]*)",r"\1a\2@@@@",wc)

        wc=re.sub(r"([a-z]*)ǘ([a-z]*)",r"\1v\2@@",wc)
        wc=re.sub(r"([a-z]*)ǚ([a-z]*)",r"\1v\2@@@",wc)
        wc=re.sub(r"([a-z]*)ǜ([a-z]*)",r"\1v\2@@@@",wc)

        wc=re.sub(r"ü",r"v",wc)

        wc=re.sub(r"([a-z]+)(\s)",r"\1@@@@@\2",wc)
        wc=re.sub(r"([a-z]+)$",r"\1@@@@@",wc)
        wc=re.sub(r"@@@@@",r"5",wc)
        wc=re.sub(r"@@@@",r"4",wc)
        wc=re.sub(r"@@@",r"3",wc)
        wc=re.sub(r"@@",r"2",wc)
        wc=re.sub(r"@",r"1",wc)

        #print(wc)

        # # 存檔
        # with open(self.output,mode="w",encoding="utf-8") as outfile:
        #     outfile.write(wc)

        return wc  #拋出內容，內容不只存檔，可直接引用，引用結果不用再開啟檔案。


if __name__ == "__main__":
    Pinyin2Pinyin()