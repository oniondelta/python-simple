
with open("input_rd.txt",mode="r",encoding="utf-8") as infile:
    strin=infile.read()

#listB = ['b','c','d','b','c','a','a','z']

#listB=list(strin) #一個字一個字分開
listA=strin.split('\n') #以\n為分割單元
#print(listA)



def deleteDuplicatedElementFromList3(listA):
    return list(set(listA)) #快超級多，但打亂原先排序
#    return sorted(set(listA), key = listA.index) #不打亂排序，但慢了至少十倍以上（約一分至兩分鐘的轉檔時間）


#以下這兩行也可
#outlist=deleteDuplicatedElementFromList3(listB)
#strout="\n".join(outlist) #必須把 列表（list）轉成 字串（string），才可輸出成檔案！
#等同上兩行
strout="\n".join(deleteDuplicatedElementFromList3(listA))



#print(strout)
with open("output_3.txt",mode="w",encoding="utf-8") as outfile:
    outfile.write(strout)