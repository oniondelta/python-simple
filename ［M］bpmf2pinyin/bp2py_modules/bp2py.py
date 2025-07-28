import re


class Bpmf2Pinyin():
    # def __init__(self,input,output):
    #     self.input=input
    #     self.output=output
    # def run_code(self):
    #     with open(self.input,mode="r",encoding="utf-8") as infile:
    #         word=infile.read()

    def run_code(words):

        wc=re.sub(r"([ㄓㄔㄕㄖㄗㄘㄙㄧㄨㄩㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦ])(\s|$)",r"\1@1\2",words)
        wc=re.sub(r"[@][1]|ˉ",r"1",wc)
        bpmf={"ˊ":"2","ˇ":"3","ˋ":"4","˙":"5"}
        for b in bpmf.keys():
            wc=re.sub(b,bpmf[b],wc)
        # wc=re.sub(r"ˊ",r"2",wc)
        # wc=re.sub(r"ˇ",r"3",wc)
        # wc=re.sub(r"ˋ",r"4",wc)
        # wc=re.sub(r"˙",r"5",wc)

        wc=re.sub(r"ㄌㄩㄢ(\d|\s)",r"lvan\1",wc)
        wc=re.sub(r"ㄋㄩㄝ(\d|\s)",r"nve\1",wc)
        wc=re.sub(r"ㄌㄩㄝ(\d|\s)",r"lve\1",wc)
        wc=re.sub(r"ㄋㄩ(\d|\s)",r"nv\1",wc)
        wc=re.sub(r"ㄌㄩ(\d|\s)",r"lv\1",wc)

        # bpmf=["ㄅ","ㄆ","ㄇ","ㄈ","ㄉ","ㄊ","ㄋ","ㄌ","ㄍ","ㄎ","ㄏ","ㄐ","ㄑ","ㄒ"]
        # pinyin=["b","p","m","f","d","t","n","l","g","k","h","j","q","x"]
        bpmf={"ㄅ":"b","ㄆ":"p","ㄇ":"m","ㄈ":"f","ㄉ":"d","ㄊ":"t","ㄋ":"n","ㄌ":"l","ㄍ":"g","ㄎ":"k","ㄏ":"h","ㄐ":"j","ㄑ":"q","ㄒ":"x"}
        for b in bpmf.keys():
            wc=re.sub(b,bpmf[b],wc)

        # wc=re.sub(r"ㄅ",r"b",wc)
        # wc=re.sub(r"ㄆ",r"p",wc)
        # wc=re.sub(r"ㄇ",r"m",wc)
        # wc=re.sub(r"ㄈ",r"f",wc)
        # wc=re.sub(r"ㄉ",r"d",wc)
        # wc=re.sub(r"ㄊ",r"t",wc)
        # wc=re.sub(r"ㄋ",r"n",wc)
        # wc=re.sub(r"ㄌ",r"l",wc)
        # wc=re.sub(r"ㄍ",r"g",wc)
        # wc=re.sub(r"ㄎ",r"k",wc)
        # wc=re.sub(r"ㄏ",r"h",wc)
        # wc=re.sub(r"ㄐ",r"j",wc)
        # wc=re.sub(r"ㄑ",r"q",wc)
        # wc=re.sub(r"ㄒ",r"x",wc)

        wc=re.sub(r"ㄓ(\d|\s)",r"zhi\1",wc)
        wc=re.sub(r"ㄔ(\d|\s)",r"chi\1",wc)
        wc=re.sub(r"ㄕ(\d|\s)",r"shi\1",wc)
        wc=re.sub(r"ㄖ(\d|\s)",r"ri\1",wc)
        wc=re.sub(r"ㄗ(\d|\s)",r"zi\1",wc)
        wc=re.sub(r"ㄘ(\d|\s)",r"ci\1",wc)
        wc=re.sub(r"ㄙ(\d|\s)",r"si\1",wc)
        bpmf={"ㄓ":"zh","ㄔ":"ch","ㄕ":"sh","ㄖ":"r","ㄗ":"z","ㄘ":"c","ㄙ":"s"}
        for b in bpmf.keys():
            wc=re.sub(b,bpmf[b],wc)
        # wc=re.sub(r"ㄓ",r"zh",wc)
        # wc=re.sub(r"ㄔ",r"ch",wc)
        # wc=re.sub(r"ㄕ",r"sh",wc)
        # wc=re.sub(r"ㄖ",r"r",wc)
        # wc=re.sub(r"ㄗ",r"z",wc)
        # wc=re.sub(r"ㄘ",r"c",wc)
        # wc=re.sub(r"ㄙ",r"s",wc)

        wc=re.sub(r"(^|\n|[ \t12345])ㄧㄚ",r"\1ya",wc) #「^」只在文件開頭，一行的開頭為\n
        wc=re.sub(r"(^|\n|[ \t12345])ㄧㄛ",r"\1yo",wc)
        wc=re.sub(r"(^|\n|[ \t12345])ㄧㄝ",r"\1ye",wc)
        wc=re.sub(r"(^|\n|[ \t12345])ㄧㄞ",r"\1yai",wc)
        wc=re.sub(r"(^|\n|[ \t12345])ㄧㄠ",r"\1yao",wc)
        wc=re.sub(r"(^|\n|[ \t12345])ㄧㄡ",r"\1you",wc)
        wc=re.sub(r"(^|\n|[ \t12345])ㄧㄢ",r"\1yan",wc)
        wc=re.sub(r"(^|\n|[ \t12345])ㄧㄣ",r"\1yin",wc)
        wc=re.sub(r"(^|\n|[ \t12345])ㄧㄤ",r"\1yang",wc)
        wc=re.sub(r"(^|\n|[ \t12345])ㄧㄥ",r"\1ying",wc)
        wc=re.sub(r"(^|\n|[ \t12345])ㄨㄚ",r"\1wa",wc)
        wc=re.sub(r"(^|\n|[ \t12345])ㄨㄛ",r"\1wo",wc)
        wc=re.sub(r"(^|\n|[ \t12345])ㄨㄞ",r"\1wai",wc)
        wc=re.sub(r"(^|\n|[ \t12345])ㄨㄟ",r"\1wei",wc)
        wc=re.sub(r"(^|\n|[ \t12345])ㄨㄢ",r"\1wan",wc)
        wc=re.sub(r"(^|\n|[ \t12345])ㄨㄣ",r"\1wen",wc)
        wc=re.sub(r"(^|\n|[ \t12345])ㄨㄤ",r"\1wang",wc)
        wc=re.sub(r"(^|\n|[ \t12345])ㄨㄥ",r"\1weng",wc)
        wc=re.sub(r"(^|\n|[ \t12345])ㄩㄝ",r"\1yue",wc)
        wc=re.sub(r"(^|\n|[ \t12345])ㄩㄢ",r"\1yuan",wc)
        wc=re.sub(r"(^|\n|[ \t12345])ㄩㄣ",r"\1yun",wc)
        wc=re.sub(r"(^|\n|[ \t12345])ㄩㄥ",r"\1yong",wc)

        bpmf={"ㄧㄝ":"ie","ㄧㄡ":"iu","ㄧㄣ":"in","ㄧㄥ":"ing","ㄨㄟ":"ui","ㄨㄣ":"un","ㄨㄥ":"ong","ㄩㄝ":"ue","ㄩㄣ":"un","ㄩㄥ":"iong"}
        for b in bpmf.keys():
            wc=re.sub(b,bpmf[b],wc)
        # wc=re.sub(r"ㄧㄝ",r"ie",wc)
        # wc=re.sub(r"ㄧㄡ",r"iu",wc)
        # wc=re.sub(r"ㄧㄣ",r"in",wc)
        # wc=re.sub(r"ㄧㄥ",r"ing",wc)
        # wc=re.sub(r"ㄨㄟ",r"ui",wc)
        # wc=re.sub(r"ㄨㄣ",r"un",wc)
        # wc=re.sub(r"ㄨㄥ",r"ong",wc)
        # wc=re.sub(r"ㄩㄝ",r"ue",wc)
        # wc=re.sub(r"ㄩㄣ",r"un",wc)
        # wc=re.sub(r"ㄩㄥ",r"iong",wc)

        wc=re.sub(r"(^|\n|[ \t12345])ㄧ([ \t12345])",r"\1yi\2",wc)
        wc=re.sub(r"(^|\n|[ \t12345])ㄨ([ \t12345])",r"\1wu\2",wc)
        wc=re.sub(r"(^|\n|[ \t12345])ㄩ([ \t12345])",r"\1yu\2",wc)
        bpmf={"ㄧ":"i","ㄨ":"u","ㄩ":"u","ㄚ":"a","ㄛ":"o","ㄜ":"e","ㄝ":"eh","ㄞ":"ai","ㄟ":"ei","ㄠ":"ao","ㄡ":"ou","ㄢ":"an","ㄣ":"en","ㄤ":"ang","ㄥ":"eng","ㄦ":"er"}
        for b in bpmf.keys():
            wc=re.sub(b,bpmf[b],wc)
        # wc=re.sub(r"ㄧ",r"i",wc)
        # wc=re.sub(r"ㄨ",r"u",wc)
        # wc=re.sub(r"ㄩ",r"u",wc)

        # wc=re.sub(r"ㄚ",r"a",wc)
        # wc=re.sub(r"ㄛ",r"o",wc)
        # wc=re.sub(r"ㄜ",r"e",wc)
        # wc=re.sub(r"ㄝ",r"eh",wc)
        # wc=re.sub(r"ㄞ",r"ai",wc)
        # wc=re.sub(r"ㄟ",r"ei",wc)
        # wc=re.sub(r"ㄠ",r"ao",wc)
        # wc=re.sub(r"ㄡ",r"ou",wc)
        # wc=re.sub(r"ㄢ",r"an",wc)
        # wc=re.sub(r"ㄣ",r"en",wc)
        # wc=re.sub(r"ㄤ",r"ang",wc)
        # wc=re.sub(r"ㄥ",r"eng",wc)
        # wc=re.sub(r"ㄦ",r"er",wc)

        wc=re.sub(r"([ \t12345])(5)([a-z]+)",r"\1\3\2",wc) #輕聲在前時換到後面
        wc=re.sub(r"51",r"5",wc) #輕聲在前置後時，出現的bug除錯
        wc=re.sub(r"(\d)([a-z])",r"\1 \2",wc) #無空格增加空格

        #print(wc)

        # # 存檔
        # with open(self.output,mode="w",encoding="utf-8") as outfile:
        #     outfile.write(wc)

        return wc  #拋出內容，內容不只存檔，可直接引用，引用結果不用再開啟檔案。


if __name__ == "__main__":
    Bpmf2Pinyin()