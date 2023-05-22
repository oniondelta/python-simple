#coding=utf-8
import re

with open("input_rd.txt",mode="r",encoding="utf-8") as infile:
    strin=infile.read()

listA=strin.split('\n') #以\n為分割單元


def dictWay2(listA):
    d = {}
    for i in listA:
        i_k = re.sub(r"\t.+", r"", i)
        i_v = re.sub(r"^.+\t", r"", i)
        d[i_k] = i_k +"\t"+ i_v
    return list(d.values())

# #print(dictWay2(listA))
strout="\n".join(dictWay2(listA))

with open("output_6.txt",mode="w",encoding="utf-8") as outfile:
    outfile.write(strout)