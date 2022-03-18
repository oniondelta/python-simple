# 效果等同先跑一次名稱排序，再排字數排序！
import re

class sort_by_word_count_2():
    with open("rd_ok.txt",mode="r",encoding="utf-8") as infile:
        word=infile.read()

    listword=word.split('\n') # list化
    # listword=re.split('\t|\n',word) #可分割多個字符

    while '' in listword: # 移除空白行
        listword.remove('')

    l1=[re.sub(r"\t.*$|\s.*$",r"",i) for i in listword] # 刪除後面編碼，計算前面字數
    # l2=[re.sub(r".+\t(.*)$",r"\1",i) for i in listword]

    lenl1=[len(line) for line in l1]
    # lenl1=[len(line.split()) for line in lenl1] #原範例 有 split 此處不用
    # lenl1=len(l1) #會計算所有個數（裡面tuple的個數，如是string則會計算所有字數）

    listall=list(zip(lenl1,listword)) #合併字數列和原文 #該合併不會合併相同的

    # listall=sorted(listall,key=lambda x:x[0]) #按字數調整順序 # 與 excel 相同，不打亂原先順序
    # listall.sort(key=lambda x:x[0]) #功能同上
    listall=sorted(listall) #按字數調整順序 #會打亂原先順序，非一一遞補，名稱一起排序
    # listall=sorted(listall,key=len) #只能針對單純list，複合list無法使用參數 key=len

    n, v = zip(*listall) #轉回兩個 list (實際是兩個 tuple)
    # print(type(n))
    # print(type(v))
    v="\n".join(v) # 轉成字串（string）形式
    # print(v)

    with open("output_finish.txt",mode="w",encoding="utf-8") as outfile:
        outfile.write(v)

if __name__ == "__main__":
    sort_by_word_count_2()