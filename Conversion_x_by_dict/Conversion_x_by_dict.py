import re

with open("input_main.txt",mode="r",encoding="utf-8") as infile:
    word=infile.read()

with open("conversion_dict.txt",mode="r",encoding="utf-8") as indict:
    change=eval(indict.read())  #讀取的str轉換為字典

#bpmf={"ㄅ":"b","ㄆ":"p","ㄇ":"m","ㄈ":"f","ㄉ":"d","ㄊ":"t","ㄋ":"n","ㄌ":"l","ㄍ":"g","ㄎ":"k","ㄏ":"h","ㄐ":"j","ㄑ":"q","ㄒ":"x"}
for b in change.keys():
    word=re.sub(b,change[b],word)

with open("output_main.txt",mode="w",encoding="utf-8") as outfile:
    outfile.write(word)