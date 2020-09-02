
import re
# from collections import Counter

with open("input_retain.txt",mode="r",encoding="utf-8") as infile:
    lists=infile.read()

with open("retain_list.txt",mode="r",encoding="utf-8") as inlist:
    retain=eval(inlist.read())  #讀取的str轉換為「列表」

listsretain=lists.split('\n')

# 找出保留retain列表中的元素（製作 output_retain）
result1=[]
for i in listsretain:
    for j in retain:
        if re.findall( j, i):
            result1.append(i)

# 把retain列表中的元素去除重複。
def dictWay2(l1):
    d = {}
    for i in l1:
        d[i] = None
    return list(d.keys())

# 製作 把含有保留retain列表中的元素轉成@，然後移除。（製作 output_other）
v1=['@']*len(retain)
retain=dict(zip(retain,v1))
result2=lists
for b in retain.keys():
    result2=re.sub(b,retain[b],result2)
result2=re.sub(r'.*[@].*(\n|$)',r'',result2)

# result2=result2.split('\n')
# result2=[re.sub(r'^.*[@].*',r'',ii) for ii in result2]
# while '' in result2:
#     result2.remove('')

# 以下會導出重複詞條
# result2=[]
# for i in lists:
#     for j in retain:
#         # result2=re.sub(j,r'@@@',i)
#         result2.append(re.sub(j,r'@@@',i))
# result2=[re.sub(r'^.*[@][@][@].*',r'',ii) for ii in result2]
# while '' in result2:
#     result2.remove('')

result1="\n".join(dictWay2(result1))
# result2="\n".join(result2)

with open("output_retain.txt",mode="w",encoding="utf-8") as outfile:
    outfile.write(result1)

with open("output_other.txt",mode="w",encoding="utf-8") as outfile:
    outfile.write(result2)






