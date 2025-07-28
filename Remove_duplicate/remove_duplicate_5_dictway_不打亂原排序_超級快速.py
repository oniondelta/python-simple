#coding=utf-8

with open("input_rd.txt",mode="r",encoding="utf-8") as infile:
    strin=infile.read()

listA=strin.split('\n') #以\n為分割單元



def dictWay2(listA):
    d = {}
    for i in listA:
        d[i] = None
    return list(d.keys())


#print(dictWay2(listA))
strout="\n".join(dictWay2(listA))

with open("output_5.txt",mode="w",encoding="utf-8") as outfile:
    outfile.write(strout)