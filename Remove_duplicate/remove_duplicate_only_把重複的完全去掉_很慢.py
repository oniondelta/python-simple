
with open("input_rd.txt",mode="r",encoding="utf-8") as infile:
    strin=infile.read()

#listB = ['b','c','d','b','c','a','a','z']

#listB=list(strin) #一個字一個字分開
listB=strin.split('\n') #以\n為分割單元
#print(strin)

# Method_#1 （超快速，好！）
from collections import Counter
# key: element
# value: occurrence of element
num_occ_dict = Counter(listB)
element_only_once = [ elem for elem in num_occ_dict if num_occ_dict[elem] == 1] #總共出現「1」次的對映就是最後結果，故兩次以上全都不收錄
##print("Elements occurs only once:", element_only_once)

# Method_#2（極度慢！！！）
#element_only_once = [ elem for elem in listB if listB.count(elem) == 1 ]
##print("Elements occurs only once:", element_only_once)


strout="\n".join(element_only_once) #必須把 列表（list）轉成 字串（string），才可輸出成檔案！

#print(strout)
with open("output_only.txt",mode="w",encoding="utf-8") as outfile:
    outfile.write(strout)