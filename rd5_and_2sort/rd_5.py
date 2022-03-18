#coding=utf-8


def dictWay2(listA):
    d = {}
    for i in listA:
        d[i] = None
    return list(d.keys())

class remove_duplicate_5():
    with open("input_dict.txt",mode="r",encoding="utf-8") as infile:
        strin=infile.read()

    listA=strin.split('\n') #以\n為分割單元

    #print(dictWay2(listA))
    strout="\n".join(dictWay2(listA))

    with open("rd_ok.txt",mode="w",encoding="utf-8") as outfile:
        outfile.write(strout)


if __name__ == "__main__":
    remove_duplicate_5()