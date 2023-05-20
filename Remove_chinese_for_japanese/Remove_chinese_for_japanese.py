
import re

with open("input_remove_ch.txt",mode="r",encoding="utf-8") as infile:
    lists=infile.read()

listtext=lists.split('\n')

# 移除 [x00-x7f] 匹配ASCII值从0-127的字符
# listtext=[re.sub(u'^[^\t]*[\x00-\x7F][^\t]*\t.+$',r'',ii) for ii in listtext]
listtext=[re.sub(u'^.*[\x00-\x7F].*$',r'',ii) for ii in listtext]
# 移除 CJK
# listtext=[re.sub(u'^[^\t]*[\u4E00-\u9FFF][^\t]*\t.+$',r'',ii) for ii in listtext]
listtext=[re.sub(u'^.*[\u4E00-\u9FFF].*$',r'',ii) for ii in listtext]
# 移除 ExtA
# listtext=[re.sub(u'^[^\t]*[\u3400-\u4DBF][^\t]*\t.+$',r'',ii) for ii in listtext]
listtext=[re.sub(u'^.*[\u3400-\u4DBF].*$',r'',ii) for ii in listtext]
# 移除 ExtB
# listtext=[re.sub(u'^[^\t]*[\u20000-\u2A6DF][^\t]*\t.+$',r'',ii) for ii in listtext]
listtext=[re.sub(u'^.*[\u20000-\u2A6DF].*$',r'',ii) for ii in listtext]
# 移除 ExtC
# listtext=[re.sub(u'^[^\t]*[\u2A700-\u2B73F][^\t]*\t.+$',r'',ii) for ii in listtext]
listtext=[re.sub(u'^.*[\u2A700-\u2B73F].*$',r'',ii) for ii in listtext]
# 移除 ExtD
# listtext=[re.sub(u'^[^\t]*[\u2B740-\u2B81F][^\t]*\t.+$',r'',ii) for ii in listtext]
listtext=[re.sub(u'^.*[\u2B740-\u2B81F].*$',r'',ii) for ii in listtext]
# 移除 ExtE
# listtext=[re.sub(u'^[^\t]*[\u2B820-\u2CEAF][^\t]*\t.+$',r'',ii) for ii in listtext]
listtext=[re.sub(u'^.*[\u2B820-\u2CEAF].*$',r'',ii) for ii in listtext]
# 移除 Compat 相容漢字
# listtext=[re.sub(u'^[^\t]*[\u2F800-\u2FA1F][^\t]*\t.+$',r'',ii) for ii in listtext]
listtext=[re.sub(u'^.*[\u2F800-\u2FA1F].*$',r'',ii) for ii in listtext]


# 移除 空白行
#listtext=[re.sub(r'^\s',r'',ii) for ii in listtext]

#超級慢#
# while '' in listtext:
#     listtext.remove('')

# result1=[]
# for i in listtext:
#     if i=''

#listtext=lists
# result1=[]
# for i in listtext:
#     i=


listtext="\n".join(listtext)

# 移除 空白行
listtext=re.sub(r'\n{2,}',r'\n',listtext)

with open("output_remove_ch.txt",mode="w",encoding="utf-8") as outfile:
    outfile.write(listtext)







