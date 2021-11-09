
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
array30_words_d="\n".join(array30_words)

# 轉成 dict 前，必須先去除空行
array30_words_d = re.sub(r"^\n+",r"",array30_words_d)
array30_words_d = re.sub(r"\n$",r"",array30_words_d)
array30_words_d = re.sub(r"[\n]+",r"\n",array30_words_d)

# 字串轉成 dict 形式（執行只保留第一碼）
# b={'a':'好','dd':'天','a':'可','a':'大','dd':'小'}
# print(b)
array30_words_d = re.sub(r"\n",r"','",array30_words_d)
array30_words_d = re.sub(r"\t",r"':'",array30_words_d)
array30_words_d = "{\n'" + array30_words_d + "'\n}"
array30_words_d = eval(array30_words_d)



# 照原來順序排列
# new_dic = {v : k for k, v in array30_words_d.items()} #把字典 key 和 value 顛倒調換
array30_words.reverse()
array30_words = [re.sub(r'\t.+$', r'', ii) for ii in array30_words]

def S_dict(listA,dictA):
    d = {}
    for i in listA:
        try:
            d[i] = dictA[i]
            # print(d)
        except KeyError:
            d[i] = None
            del d[i]
            print('有錯誤，有缺！！！')
    return d #d.keys() #list(d.keys())

array30_words_out = S_dict( array30_words, array30_words_d)
# print(S_dict(array30_words,new_dic))
# print(array30_words)
# print(array30_words_out)
# print(S_dict(array30_words,array30_words_d))



# dict 轉回 str 形式
array30_words_out = str(array30_words_out)
array30_words_out = re.sub(r"[{'}]",r"",array30_words_out)
array30_words_out = re.sub(r", ",r"\n",array30_words_out)
array30_words_out = re.sub(r": ",r"\t",array30_words_out)

# 行列30詞尾綴「!」轉回「'」
# array30_words_out = re.sub(r"!",r"'",array30_words_out)


array30_words_out=array30_words_out.split('\n')
# array30_words_out.reverse()
array30_words_out=[re.sub(r'^(.+)\t(.+)', r'\2\t\1', ii) for ii in array30_words_out]
array30_words_out = "\n".join(array30_words_out)


# print(array30_words_out)



#輸出 .txt 檔案
with open("output_array30_words_original-order.txt",mode="w",encoding="utf-8") as out_file:
    out_file.write(array30_words_out)