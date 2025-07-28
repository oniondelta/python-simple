#coding=utf-8


def dictWay2(listA):
    d = {}
    for i in listA:
        d[i] = None
    return list(d.keys())


class RemoveDuplicate5():
    # def __init__(self,input,output):
    #     self.input=input
    #     self.output=output
    # def run_code(self):
    #     with open(self.input,mode="r",encoding="utf-8") as infile:
    #         strin=infile.read()

    def run_code(strin):

        listA=strin.split('\n') #以\n為分割單元

        #print(dictWay2(listA))
        strout="\n".join(dictWay2(listA))

        # with open(self.output,mode="w",encoding="utf-8") as outfile:
        #     outfile.write(strout)

        return strout


if __name__ == "__main__":
    RemoveDuplicate5()