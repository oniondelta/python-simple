
import re

#讀入檔案
with open("input_array30_words.txt",mode="r",encoding="utf-8") as in_file:
    array30_words=in_file.read()
    # array30_words=eval(in_file.read())  #讀取的str轉換為「字典」

# 行列30詞尾綴「'」轉成「!」
# array30_words = re.sub(r"'",r"!",array30_words)

# str 轉成 list 形式
array30_words = re.sub(r"\n",r"','",array30_words)
array30_words = "[\n'" + array30_words + "'\n]"
array30_words = eval(array30_words)
array30_words.reverse()
array30_words=[re.sub(r'^(.+)\t(.+)', r'\2\t\1', ii) for ii in array30_words]

# list 轉換回 str
array30_words="\n".join(array30_words)

# 轉成 dict 前，必須先去除空行
array30_words = re.sub(r"^\n+",r"",array30_words)
array30_words = re.sub(r"\n$",r"",array30_words)
array30_words = re.sub(r"[\n]+",r"\n",array30_words)

# 字串轉成 dict 形式（執行只保留第一碼）
# b={'a':'好','dd':'天','a':'可','a':'大','dd':'小'}
# print(b)
array30_words = re.sub(r"\n",r"','",array30_words)
array30_words = re.sub(r"\t",r"':'",array30_words)
array30_words = "{\n'" + array30_words + "'\n}"
array30_words = eval(array30_words)

# dict 轉回 str 形式
array30_words = str(array30_words)
array30_words = re.sub(r"[{'}]",r"",array30_words)
array30_words = re.sub(r", ",r"\n",array30_words)
array30_words = re.sub(r": ",r"\t",array30_words)

# 行列30詞尾綴「!」轉回「'」
# array30_words = re.sub(r"!",r"'",array30_words)


array30_words=array30_words.split('\n')
array30_words.reverse()
array30_words=[re.sub(r'^(.+)\t(.+)', r'\2\t\1', ii) for ii in array30_words]
array30_words = "\n".join(array30_words)


# print(array30_words)



#輸出 .txt 檔案
with open("output_array30_words.txt",mode="w",encoding="utf-8") as out_file:
    out_file.write(array30_words)