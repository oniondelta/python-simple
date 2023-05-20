## 各種轉換

# import jaconv
# import convrules_onion
import convrules_jp_hanji_freq
import re


# j1=re.compile(r'[あいうえおゐゑぁぃぅぇぉかきくけこがぎぐげごゕゖさしすせそざじずぜぞたちつてとだぢづでどっなにぬねのはひふへほばびぶべぼゔぱぴぷぺぽまみむめもやゆよゃゅょらりるれろわをんゎ・ー=]') #ー
# j2=re.compile(r'[アイウエオヰヱァィゥェォカキクケコガギグゲゴヵヶサシスセソザジズゼゾタチツテトダヂヅデドッナニヌネノハヒフヘホバビブベボヴパピプペポマミムメモヤユヨャュョラリルレロワヲンヮ・ー=]') #ー
j3=re.compile(u'^[ゝゞヽヾ、。゠=・ー〆々あいうえおゐゑぁぃぅぇぉかきくけこがぎぐげごゕゖさしすせそざじずぜぞたちつてとだぢづでどっなにぬねのはひふへほばびぶべぼゔぱぴぷぺぽまみむめもやゆよゃゅょらりるれろわをんゎアイウエオヰヱァィゥェォカキクケコガギグゲゴヵヶサシスセソザジズゼゾタチツテトダヂヅデドッナニヌネノハヒフヘホバビブベボヴパピプペポマミムメモヤユヨャュョラリルレロワヲンヮ]+\t')
# j3=re.compile(u'^[\u3040-\u309f\u30a0-\u30ff\u3001\u3002\u3005\u3006\u003d]+\t')
# j3=re.compile(u'^[\u30a0-\u30ff\u3040-\u309f]+')
en_upper=re.compile(r'\t[A-Z]')


### 保留純假名詞條 ###
def RESERVE_KANA(KANA, EN_U, outlist, index, inline):
  ## re.match v.s. re.search
  ##   re.match只匹配字符串的開始，如果字符串開始不符合正則表達式，則匹配失败，函数返回None；
  ##   re.search匹配整个字符串，直到找到一個匹配。
  if re.match(KANA, inline) and not re.search(EN_U, inline):
    inline=re.sub(r"\t.+\t", r"\t", inline)
    # res=re.findall('[\u3040-\u309f|\u30a0-\u30ff|\u3001|\u3002|\u3005|\u3006|\u003d]',inline)
    # print(inline)
    outlist[index]=inline
  else:
    outlist[index] = ""
    # del outlist[index] #用 index 會有依序問題！後會整個會亂掉！


### 去除純假名詞條（與上面反過來） ###
def REMOVE_KANA(KANA, outlist, index, inline):
  if re.match(KANA, inline):
    outlist[index] = ""
  else:
    inline=re.sub(r" ", r"", inline)
    # inline=re.sub(r"\t(?=\d)", r"@@", inline)
    outlist[index]=inline


### 詞條置換成詞頻 ###
## 詞條頭尾需是「@」，如：「@亀川  kamegawa@」
def REPLACE_FREQUENCY(outlist, index, inline):
  for convert_rule in convrules_jp_hanji_freq.CONVERT_PATTERN_HANJI:
    if inline == convert_rule[0]:
      inline = inline.replace(convert_rule[0], convert_rule[1])
      outlist[index]=inline
      print(index)
      break
      # break：強制跳出 ❮整個❯ 迴圈
      # continue：強制跳出 ❮本次❯ 迴圈，繼續進入下一圈。跳過執行以下程式碼執行，然後繼續迴圈。
      # pass：不做任何事情，所有的程式都將繼續
    # else:
    #   continue


### 各種移除轉換符號 ###
def REMOVE_SIGN(outlist, index, inline):
  ## 移除符號，使編碼羅馬字母連續
  inline=re.sub(r"[ ;.,]", r"", inline)
  # inline=re.sub(r"(?<=[a-z-/])[ ;.,]", r"", inline)
  inline=re.sub(r"\t\d+$", r"", inline)

  # ## 轉換符號，符合置換格式一
  # inline=re.sub(r"^", r"`", inline)
  # inline=re.sub(r"@@", r"`@@`", inline)
  # inline=re.sub(r"$", r"`", inline)

  # ## 轉換符號，符合置換格式二
  # # inline=re.sub(r"^", r"     ['", inline)
  # # inline=re.sub(r"$", r"'],", inline)
  # # inline=re.sub(r"\t(?=\d)", r"', '", inline)
  # inline=re.sub(r"\['", r"['@", inline)
  # inline=re.sub(r"', '", r"@', '", inline)

  outlist[index]=inline




with open("input_many_functions.txt",mode="r",encoding="utf-8") as infile:
    l1=infile.read()
    # l1=infile.readlines()
l1=l1.split('\n')
#print(l1)

for index, ii in enumerate(l1):
  # # 変換フォーズ1  ex. 「あ」→「a」、「りゅ」→「ryu」
  # for convert_rule in convrules_onion.CONVERT_PATTERN_ONION:
  #   ii = ii.replace(convert_rule[0], convert_rule[1])


  ### 保留純假名詞條 ###
  # RESERVE_KANA(j3, en_upper, l1, index, ii)

  ### 去除純假名詞條 ###
  # REMOVE_KANA(j3, l1, index, ii)

  ### 各種移除轉換符號 ###
  # REMOVE_SIGN(l1, index, ii)

  ### 詞條置換成詞頻 ###
  ## 詞條頭尾需是「@」，如：「@亀川  kamegawa@」
  REPLACE_FREQUENCY(l1, index, ii)


# ## 去除空行
# l1 = list(filter(None, l1))


#print(l1)
strout="\n".join(l1)

with open("output_many_functions.txt",mode="w",encoding="utf-8") as outfile:
    outfile.write(strout)
