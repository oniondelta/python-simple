## 各種轉換

# import jaconv
# import convrules_onion
import convrules_jp_hanji_freq
import convrules_jp_hanji_freq_2
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


def REPLACE_FREQUENCY_2(outlist, index, inline):
  if re.match(r'@', inline):

    for convert_rule in convrules_jp_hanji_freq_2.CONVERT_PATTERN_HANJI_2:
      if inline == convert_rule[0]:
        inline = inline.replace(convert_rule[0], convert_rule[1])
        outlist[index]=re.sub(r"@", r"",outlist[index])+"\t"+inline
        # outlist[index]=inline
        print(index)
        break
        # break：強制跳出 ❮整個❯ 迴圈
        # continue：強制跳出 ❮本次❯ 迴圈，繼續進入下一圈。跳過執行以下程式碼執行，然後繼續迴圈。
        # pass：不做任何事情，所有的程式都將繼續
      # else:
      #   continue

  else:
    print("no:",index)


### 各種移除轉換符號 ###
def REMOVE_SIGN(outlist, index, inline):
  ## 移除符號，使編碼羅馬字母連續
  inline=re.sub(r"[ ;.,`]", r"", inline)
  # inline=re.sub(r"(?<=[a-z-/])[ ;.,]", r"", inline)
  # inline=re.sub(r"\t\d+$", r"", inline)

  # inline=re.sub(r"^(.+[^\d])$", r"@\1@", inline)

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


### 轉換外來語假名 ###
def REPLACE_GKK_KANA(outlist, index, inline):

  inline=re.sub(r"ty([auoie])([.,])", r"chi\2 x\1\2", inline) #ちぇ
  inline=re.sub(r"th([ie])([.,])", r"te\2 xi\1\2", inline) #てぃ、てぇ
  inline=re.sub(r"tw([auoie])([.,])", r"to\2 x\1\2", inline) #とぁ、とぅ、とぉ、とぃ、とぇ
  inline=re.sub(r"dh([ie])([.,])", r"de\2 x\1\2", inline) #でぃ、でぇ
  inline=re.sub(r"dh([auo])([.,])", r"de\2 xy\1\2", inline) #でゅ、でゅ、でょ
  inline=re.sub(r"by([auo])([.,])", r"bi\2 xy\1\2", inline) #びゃ、びゅ、びょ
  inline=re.sub(r"hy([auo])([.,])", r"hi\2 xy\1\2", inline) #ひゃ、ひゅ、ひょ
  inline=re.sub(r"ny([auo])([.,])", r"ni\2 xy\1\2", inline) #にゃ、にゅ、にょ
  inline=re.sub(r"gy([auo])([.,])", r"gi\2 xy\1\2", inline) #ぎゃ、ぎゅ、ぎょ
  inline=re.sub(r"dy([auo])([.,])", r"di\2 xy\1\2", inline) #ぢゃ、ぢゅ、ぢょ
  inline=re.sub(r"dy([ie])([.,])", r"di\2 x\1\2", inline) #ぢぃ、ぢぇ
  inline=re.sub(r"j([auo])([.,])", r"ji\2 xy\1\2", inline) #じゃ、じゅ、じょ
  inline=re.sub(r"j([e])([.,])", r"ji\2 x\1\2", inline) #じぇ
  inline=re.sub(r"f([aoe])([.,])", r"fu\2 x\1\2", inline) #ふぁ、ふぉ、ふぇ
  inline=re.sub(r"ts([oeia])([.,])", r"tsu\2 x\1\2", inline) #つぉ、つぇ、つぃ、つぁ
  inline=re.sub(r"sy(i)([.,])", r"shi\2 x\1\2", inline) #しぃ
  inline=re.sub(r"gw([auoei])([.,])", r"gu\2 x\1\2", inline) #ぐゎ、ぐぅ、ぐぉ、ぐぇ、ぐぃ
  inline=re.sub(r"wh([auoei])([.,])", r"u\2 x\1\2", inline) #うぁ、うぅ、うぉ、うぇ、うぃ

  outlist[index]=inline



def main():
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

    ### 轉換外來語假名 ###
    REPLACE_GKK_KANA(l1, index, ii)

    # ### 詞條置換成詞頻(以分割之促音，如：「q」) ###
    # ## 詞條頭尾需是「@」，如：「@亀川  kamegawa@」
    # REPLACE_FREQUENCY(l1, index, ii)

    ### 詞條置換成詞頻(以相連之促音，如：「tta」) ###
    ## 詞條頭尾需是「@」，如：「@亀川  kamegawa@」
    # REPLACE_FREQUENCY_2(l1, index, ii)


  # ## 去除空行
  # l1 = list(filter(None, l1))


  #print(l1)
  strout="\n".join(l1)

  with open("output_many_functions.txt",mode="w",encoding="utf-8") as outfile:
    outfile.write(strout)


if __name__ == "__main__":
  main()
