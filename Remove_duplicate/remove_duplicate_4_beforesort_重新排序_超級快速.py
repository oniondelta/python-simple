#coding=utf-8

with open("input_rd.txt",mode="r",encoding="utf-8") as infile:
    strin=infile.read()

listA=strin.split('\n') #以\n為分割單元


def test(listA):
    n = []
    listA.sort()
    repeat = None
    for e in listA:
        if e != repeat:
            repeat = e
            n.append(e)
    return n


#print(test(listA))
strout="\n".join(test(listA))

with open("output_4.txt",mode="w",encoding="utf-8") as outfile:
    outfile.write(strout)