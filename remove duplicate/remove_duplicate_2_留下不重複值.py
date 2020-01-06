
with open("input_rd.txt",mode="r",encoding="utf-8") as infile:
    strin=infile.read()

#listA = ['b','c','d','b','c','a','a','z']
#listA=list(strin) #一個字一個字分開
listA=strin.split('\n') #以\n為分割單元
#print(listA)


def deleteDuplicatedElementFromList2(listA):
    resultList = []
    for item in listA:
        if not item in resultList:
            resultList.append(item)
    return resultList
#    print(resultList)

#deleteDuplicatedElementFromList2(listA) #上行用列印，使用此行可列印出來


#以下這兩行也可
#outlist=deleteDuplicatedElementFromList3(listB)
#strout="\n".join(outlist) #必須把 列表（list）轉成 字串（string），才可輸出成檔案！

#等同上兩行
strout="\n".join(deleteDuplicatedElementFromList2(listA))


#print(strout)
with open("output_2.txt",mode="w",encoding="utf-8") as outfile:
    outfile.write(strout)

