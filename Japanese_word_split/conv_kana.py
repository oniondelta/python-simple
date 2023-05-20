## 轉換成假名成指定羅馬字母

# import jaconv
import convrules_onion
import re


with open("input_kana.txt",mode="r",encoding="utf-8") as infile:
    l1=infile.read()
    # l1=infile.readlines()    #該則 list 中元素末尾會有「\n」，需處理。
l1=l1.split('\n')
# print(l1)


for index, ii in enumerate(l1):
  ii_h=ii
  # 変換フォーズ1  ex. 「あ」→「a」、「りゅ」→「ryu」
  for convert_rule in convrules_onion.CONVERT_PATTERN_ONION:
    ii = ii.replace(convert_rule[0], convert_rule[1])

  ii=re.sub(r" $", r"",ii)
  if ii != ii_h:
    ii=ii_h+"\t"+ii

  l1[index]=ii


#print(l1)
strout="\n".join(l1)

with open("output_kana.txt",mode="w",encoding="utf-8") as outfile:
    outfile.write(strout)

