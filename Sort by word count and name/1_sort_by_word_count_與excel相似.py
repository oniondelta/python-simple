with open("input_sort_count.txt",mode="r",encoding="utf-8") as infile:
    word=infile.read()

listword=word.split('\n') # list化

while '' in listword: # 移除空白行
    listword.remove('')

import re
l1=[re.sub(r"\t.*$|\s.*$",r"",i) for i in listword] # 刪除後面編碼，計算前面字數

lenl1=[len(line) for line in l1]

listall=list(zip(lenl1,listword)) # 合併字數列和原文 #該合併不會合併相同的

listall=sorted(listall,key=lambda x:x[0]) # 按字數調整順序 # 與 excel 相同，不打亂原先順序

n, v = zip(*listall) # 轉回兩個 list (實際是兩個 tuple)
v="\n".join(v) # 轉成字串（string）形式

with open("output_1_sort_count.txt",mode="w",encoding="utf-8") as outfile:
    outfile.write(v)
