
# import jaconv
import convrules_onion
import re


def main():
  with open("input_jp_split.txt",mode="r",encoding="utf-8") as infile:
      l1=infile.read()
  #    l1=infile.readlines()
  l1=l1.split('\n')
  #print(l1)


  # j1=re.compile(r'([あいうえおゐゑぁぃぅぇぉかきくけこがぎぐげごゕゖさしすせそざじずぜぞたちつてとだぢづでどっなにぬねのはひふへほばびぶべぼゔぱぴぷぺぽまみむめもやゆよゃゅょらりるれろわをんゎ])') #ー
  # j2=re.compile(r'([アイウエオヰヱァィゥェォカキクケコガギグゲゴヵヶサシスセソザジズゼゾタチツテトダヂヅデドッナニヌネノハヒフヘホバビブベボヴパピプペポマミムメモヤユヨャュョラリルレロワヲンヮ])') #ー


  for index, ii in enumerate(l1):
    # 変換フォーズ1  ex. 「あ」→「a」、「りゅ」→「ryu」
    for convert_rule in convrules_onion.CONVERT_PATTERN_ONION:
      ii = ii.replace(convert_rule[0], convert_rule[1])

    ii2=re.sub(r"[,. ]", r"", ii)

    # 假漢
    if re.match(r"^([a-z/;-]+)[^a-z/;-]+\t\1", ii2):
      abc=re.sub(r"^([a-z/,.; -]+)[^a-z/,.; -]+\t.+", r'\1', ii)
      abc=re.sub(r"[,. ]", r'', abc)
      hanji=re.sub(r"^.+\t"+abc, r'', ii)
      ii=re.sub(r"^([a-z/,.; -]+)[^a-z/,.; -]+\t", r'\1'+hanji+r";\t", ii)

    # 漢假
    elif re.match(r"^([^a-z/;-]+)([a-z/;-]+)\t.+\2$", ii2):
      abc=re.sub(r"^[^a-z/,.; -]+([a-z/,.; -]+)\t.+$", r'\1', ii)
      abc=re.sub(r"[,. ]", r'', abc)
      hanji=re.sub(r"^.+\t([a-z/;-]+)"+abc, r'\1', ii)
      ii=re.sub(r"^[^a-z/,.; -]+([a-z/,.; -]+)\t", hanji+r'; \1'+r"\t", ii)

    # 假漢假
    elif re.match(r"^([a-z/;-]+)([^a-z/;-]+)([a-z/;-]+)\t\1.+\3$", ii2):
      abc_1=re.sub(r"^([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)\t.+$", r'\1', ii)
      abc_2=re.sub(r"^([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)\t.+$", r'\2', ii)
      abc_1=re.sub(r"[,. ]", r'', abc_1)
      abc_2=re.sub(r"[,. ]", r'', abc_2)
      hanji=re.sub(r"^.+\t"+abc_1+r"([a-z/;-]+)"+abc_2+r"$", r"\1", ii)
      ii=re.sub(r"^([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)\t", r'\1'+hanji+r"; \2\t", ii)

    # 漢假漢
    elif re.match(r"^([^a-z/;-]+)([a-z/;-]+)([^a-z/;-]+)\t.+\2.+$", ii2):
      abc=re.sub(r"^[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+\t.+$", r'\1', ii)
      abc=re.sub(r"[,. ]", r'', abc)
      hanji_1=re.sub(r"^.+\t([a-z/;-]+)"+abc+r"([a-z/;-]+)"+r"$", r'\1', ii)
      hanji_2=re.sub(r"^.+\t([a-z/;-]+)"+abc+r"([a-z/;-]+)"+r"$", r'\2', ii)
      ii=re.sub(r"^[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+\t", hanji_1+r"; \1"+hanji_2+r";\t", ii)

    # 漢假漢假
    elif re.match(r"^([^a-z/;-]+)([a-z/;-]+)([^a-z/;-]+)([a-z/;-]+)\t.+\2.+\4$", ii2):
      abc_1=re.sub(r"^[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)\t.+$", r"\1", ii)
      abc_2=re.sub(r"^[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)\t.+$", r"\2", ii)
      abc_1=re.sub(r"[,. ]", r"", abc_1)
      abc_2=re.sub(r"[,. ]", r"", abc_2)
      # print(abc_1)
      # print(abc_2)
      hanji_1=re.sub(r"^.+\t([a-z/;-]+)"+abc_1+r"([a-z/;-]+)"+abc_2+r"$", r"\1", ii)
      hanji_2=re.sub(r"^.+\t([a-z/;-]+)"+abc_1+r"([a-z/;-]+)"+abc_2+r"$", r"\2", ii)
      # print(hanji_1)
      # print(hanji_2)
      ii=re.sub(r"^[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)\t", hanji_1+r"; \1"+hanji_2+r"; \2"+r"\t", ii)

    # 假漢假漢
    elif re.match(r"^([a-z/;-]+)([^a-z/;-]+)([a-z/;-]+)([^a-z/;-]+)\t\1.+\3.+$", ii2):
      abc_1=re.sub(r"^([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+\t.+$", r"\1", ii)
      abc_2=re.sub(r"^([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+\t.+$", r"\2", ii)
      abc_1=re.sub(r"[,. ]", r"", abc_1)
      abc_2=re.sub(r"[,. ]", r"", abc_2)
      # print(abc_1)
      # print(abc_2)#強いて言えば  取っ組合う  tokkumiau
      hanji_1=re.sub(r"^.+\t"+abc_1+r"([a-z/;-]+)"+abc_2+r"([a-z/;-]+)"+r"$", r"\1", ii)
      hanji_2=re.sub(r"^.+\t"+abc_1+r"([a-z/;-]+)"+abc_2+r"([a-z/;-]+)"+r"$", r"\2", ii)
      # print(hanji_1)
      # print(hanji_2)
      ii=re.sub(r"^([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+\t", r"\1"+hanji_1+r"; \2"+hanji_2+r";\t", ii)

    # 漢假漢假漢
    elif re.match(r"^([^a-z/;-]+)([a-z/;-]+)([^a-z/;-]+)([a-z/;-]+)([^a-z/;-]+)\t.+\2.+\4.+$", ii2):
      abc_1=re.sub(r"^[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+\t.+$", r"\1", ii)
      abc_2=re.sub(r"^[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+\t.+$", r"\2", ii)
      abc_1=re.sub(r"[,. ]", r"", abc_1)
      abc_2=re.sub(r"[,. ]", r"", abc_2)
      # print(abc_1)
      # print(abc_2)
      hanji_1=re.sub(r"^.+\t([a-z/;-]+)"+abc_1+r"([a-z/;-]+)"+abc_2+r"([a-z/;-]+)$", r"\1", ii)
      hanji_2=re.sub(r"^.+\t([a-z/;-]+)"+abc_1+r"([a-z/;-]+)"+abc_2+r"([a-z/;-]+)$", r"\2", ii)
      hanji_3=re.sub(r"^.+\t([a-z/;-]+)"+abc_1+r"([a-z/;-]+)"+abc_2+r"([a-z/;-]+)$", r"\3", ii)
      # print(hanji_1)
      # print(hanji_2)
      # print(hanji_3)
      ii=re.sub(r"^[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+\t", hanji_1+r"; \1"+hanji_2+r"; \2"+hanji_3+r";\t", ii)

    # 假漢假漢假
    elif re.match(r"^([a-z/;-]+)([^a-z/;-]+)([a-z/;-]+)([^a-z/;-]+)([a-z/;-]+)\t\1.+\3.+\5$", ii2):
      abc_1=re.sub(r"^([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)\t.+$", r"\1", ii)
      abc_2=re.sub(r"^([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)\t.+$", r"\2", ii)
      abc_3=re.sub(r"^([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)\t.+$", r"\3", ii)
      abc_1=re.sub(r"[,. ]", r"", abc_1)
      abc_2=re.sub(r"[,. ]", r"", abc_2)
      abc_3=re.sub(r"[,. ]", r"", abc_3)
      hanji_1=re.sub(r"^.+\t"+abc_1+r"([a-z/;-]+)"+abc_2+r"([a-z/;-]+)"+abc_3+r"$", r"\1", ii)
      hanji_2=re.sub(r"^.+\t"+abc_1+r"([a-z/;-]+)"+abc_2+r"([a-z/;-]+)"+abc_3+r"$", r"\2", ii)
      ii=re.sub(r"^([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)\t", r"\1"+hanji_1+r"; \2"+hanji_2+r"; \3\t", ii)

    # 漢假漢假漢假
    elif re.match(r"^([^a-z/;-]+)([a-z/;-]+)([^a-z/;-]+)([a-z/;-]+)([^a-z/;-]+)([a-z/;-]+)\t.+\2.+\4.+\6$", ii2):
      abc_1=re.sub(r"^[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)\t.+$", r"\1", ii)
      abc_2=re.sub(r"^[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)\t.+$", r"\2", ii)
      abc_3=re.sub(r"^[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)\t.+$", r"\3", ii)
      abc_1=re.sub(r"[,. ]", r"", abc_1)
      abc_2=re.sub(r"[,. ]", r"", abc_2)
      abc_3=re.sub(r"[,. ]", r"", abc_3)
      hanji_1=re.sub(r"^.+\t([a-z/;-]+)"+abc_1+r"([a-z/;-]+)"+abc_2+r"([a-z/;-]+)"+abc_3+r"$", r"\1", ii)
      hanji_2=re.sub(r"^.+\t([a-z/;-]+)"+abc_1+r"([a-z/;-]+)"+abc_2+r"([a-z/;-]+)"+abc_3+r"$", r"\2", ii)
      hanji_3=re.sub(r"^.+\t([a-z/;-]+)"+abc_1+r"([a-z/;-]+)"+abc_2+r"([a-z/;-]+)"+abc_3+r"$", r"\3", ii)
      ii=re.sub(r"^[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)\t", hanji_1+r"; \1"+hanji_2+r"; \2"+hanji_3+r"; \3\t", ii)

    # 假漢假漢假漢
    elif re.match(r"^([a-z/;-]+)([^a-z/;-]+)([a-z/;-]+)([^a-z/;-]+)([a-z/;-]+)([^a-z/;-]+)\t\1.+\3.+\5.+$", ii2):
      abc_1=re.sub(r"^([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+\t.+$", r"\1", ii)
      abc_2=re.sub(r"^([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+\t.+$", r"\2", ii)
      abc_3=re.sub(r"^([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+\t.+$", r"\3", ii)
      abc_1=re.sub(r"[,. ]", r"", abc_1)
      abc_2=re.sub(r"[,. ]", r"", abc_2)
      abc_3=re.sub(r"[,. ]", r"", abc_3)
      hanji_1=re.sub(r"^.+\t"+abc_1+r"([a-z/;-]+)"+abc_2+r"([a-z/;-]+)"+abc_3+r"([a-z/;-]+)$", r"\1", ii)
      hanji_2=re.sub(r"^.+\t"+abc_1+r"([a-z/;-]+)"+abc_2+r"([a-z/;-]+)"+abc_3+r"([a-z/;-]+)$", r"\2", ii)
      hanji_3=re.sub(r"^.+\t"+abc_1+r"([a-z/;-]+)"+abc_2+r"([a-z/;-]+)"+abc_3+r"([a-z/;-]+)$", r"\3", ii)
      # print(abc_3)
      ii=re.sub(r"^([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+\t", r"\1"+hanji_1+r"; \2"+hanji_2+r"; \3"+hanji_3+r"; \t", ii)
      # print(ii)

    # 漢假漢假漢假漢
    elif re.match(r"^([^a-z/;-]+)([a-z/;-]+)([^a-z/;-]+)([a-z/;-]+)([^a-z/;-]+)([a-z/;-]+)([^a-z/;-]+)\t.+\2.+\4.+\6.+$", ii2):
      abc_1=re.sub(r"^[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+\t.+$", r"\1", ii)
      abc_2=re.sub(r"^[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+\t.+$", r"\2", ii)
      abc_3=re.sub(r"^[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+\t.+$", r"\3", ii)
      abc_1=re.sub(r"[,. ]", r"", abc_1)
      abc_2=re.sub(r"[,. ]", r"", abc_2)
      abc_3=re.sub(r"[,. ]", r"", abc_3)
      hanji_1=re.sub(r"^.+\t([a-z/;-]+)"+abc_1+r"([a-z/;-]+)"+abc_2+r"([a-z/;-]+)"+abc_3+r"([a-z/;-]+)$", r"\1", ii)
      hanji_2=re.sub(r"^.+\t([a-z/;-]+)"+abc_1+r"([a-z/;-]+)"+abc_2+r"([a-z/;-]+)"+abc_3+r"([a-z/;-]+)$", r"\2", ii)
      hanji_3=re.sub(r"^.+\t([a-z/;-]+)"+abc_1+r"([a-z/;-]+)"+abc_2+r"([a-z/;-]+)"+abc_3+r"([a-z/;-]+)$", r"\3", ii)
      hanji_4=re.sub(r"^.+\t([a-z/;-]+)"+abc_1+r"([a-z/;-]+)"+abc_2+r"([a-z/;-]+)"+abc_3+r"([a-z/;-]+)$", r"\4", ii)
      ii=re.sub(r"^[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+\t", hanji_1+r"; \1"+hanji_2+r"; \2"+hanji_3+r"; \3"+hanji_4+r";\t", ii)

    # 假漢假漢假漢假
    elif re.match(r"^([a-z/;-]+)([^a-z/;-]+)([a-z/;-]+)([^a-z/;-]+)([a-z/;-]+)([^a-z/;-]+)([a-z/;-]+)\t\1.+\3.+\5.+\7$", ii2):
      abc_1=re.sub(r"^([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)\t.+$", r"\1", ii)
      abc_2=re.sub(r"^([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)\t.+$", r"\2", ii)
      abc_3=re.sub(r"^([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)\t.+$", r"\3", ii)
      abc_4=re.sub(r"^([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)\t.+$", r"\4", ii)
      abc_1=re.sub(r"[,. ]", r"", abc_1)
      abc_2=re.sub(r"[,. ]", r"", abc_2)
      abc_3=re.sub(r"[,. ]", r"", abc_3)
      abc_4=re.sub(r"[,. ]", r"", abc_4)
      # print(abc_4)
      hanji_1=re.sub(r"^.+\t"+abc_1+r"([a-z/;-]+)"+abc_2+r"([a-z/;-]+)"+abc_3+r"([a-z/;-]+)"+abc_4+r"$", r"\1", ii)
      hanji_2=re.sub(r"^.+\t"+abc_1+r"([a-z/;-]+)"+abc_2+r"([a-z/;-]+)"+abc_3+r"([a-z/;-]+)"+abc_4+r"$", r"\2", ii)
      hanji_3=re.sub(r"^.+\t"+abc_1+r"([a-z/;-]+)"+abc_2+r"([a-z/;-]+)"+abc_3+r"([a-z/;-]+)"+abc_4+r"$", r"\3", ii)
      ii=re.sub(r"^([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)\t", r"\1"+hanji_1+r"; \2"+hanji_2+r"; \3"+hanji_3+r"; \4\t", ii)

    # 漢假漢假漢假漢假
    elif re.match(r"^([^a-z/;-]+)([a-z/;-]+)([^a-z/;-]+)([a-z/;-]+)([^a-z/;-]+)([a-z/;-]+)([^a-z/;-]+)([a-z/;-]+)\t.+\2.+\4.+\6.+\8$", ii2):
      abc_1=re.sub(r"^[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)\t.+$", r"\1", ii)
      abc_2=re.sub(r"^[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)\t.+$", r"\2", ii)
      abc_3=re.sub(r"^[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)\t.+$", r"\3", ii)
      abc_4=re.sub(r"^[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)\t.+$", r"\4", ii)
      abc_1=re.sub(r"[,. ]", r"", abc_1)
      abc_2=re.sub(r"[,. ]", r"", abc_2)
      abc_3=re.sub(r"[,. ]", r"", abc_3)
      abc_4=re.sub(r"[,. ]", r"", abc_4)
      hanji_1=re.sub(r"^.+\t([a-z/;-]+)"+abc_1+r"([a-z/;-]+)"+abc_2+r"([a-z/;-]+)"+abc_3+r"([a-z/;-]+)"+abc_4+r"$", r"\1", ii)
      hanji_2=re.sub(r"^.+\t([a-z/;-]+)"+abc_1+r"([a-z/;-]+)"+abc_2+r"([a-z/;-]+)"+abc_3+r"([a-z/;-]+)"+abc_4+r"$", r"\2", ii)
      hanji_3=re.sub(r"^.+\t([a-z/;-]+)"+abc_1+r"([a-z/;-]+)"+abc_2+r"([a-z/;-]+)"+abc_3+r"([a-z/;-]+)"+abc_4+r"$", r"\3", ii)
      hanji_4=re.sub(r"^.+\t([a-z/;-]+)"+abc_1+r"([a-z/;-]+)"+abc_2+r"([a-z/;-]+)"+abc_3+r"([a-z/;-]+)"+abc_4+r"$", r"\4", ii)
      ii=re.sub(r"^[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)\t", hanji_1+r"; \1"+hanji_2+r"; \2"+hanji_3+r"; \3"+hanji_4+r"; \4\t", ii)

    # 假漢假漢假漢假漢
    elif re.match(r"^([a-z/;-]+)([^a-z/;-]+)([a-z/;-]+)([^a-z/;-]+)([a-z/;-]+)([^a-z/;-]+)([a-z/;-]+)([^a-z/;-]+)\t\1.+\3.+\5.+\7.+$", ii2):
      abc_1=re.sub(r"^([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+\t.+$", r"\1", ii)
      abc_2=re.sub(r"^([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+\t.+$", r"\2", ii)
      abc_3=re.sub(r"^([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+\t.+$", r"\3", ii)
      abc_4=re.sub(r"^([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+\t.+$", r"\4", ii)
      abc_1=re.sub(r"[,. ]", r"", abc_1)
      abc_2=re.sub(r"[,. ]", r"", abc_2)
      abc_3=re.sub(r"[,. ]", r"", abc_3)
      abc_4=re.sub(r"[,. ]", r"", abc_4)
      # print(abc_4)
      hanji_1=re.sub(r"^.+\t"+abc_1+r"([a-z/;-]+)"+abc_2+r"([a-z/;-]+)"+abc_3+r"([a-z/;-]+)"+abc_4+r"([a-z/;-]+)$", r"\1", ii)
      hanji_2=re.sub(r"^.+\t"+abc_1+r"([a-z/;-]+)"+abc_2+r"([a-z/;-]+)"+abc_3+r"([a-z/;-]+)"+abc_4+r"([a-z/;-]+)$", r"\2", ii)
      hanji_3=re.sub(r"^.+\t"+abc_1+r"([a-z/;-]+)"+abc_2+r"([a-z/;-]+)"+abc_3+r"([a-z/;-]+)"+abc_4+r"([a-z/;-]+)$", r"\3", ii)
      hanji_4=re.sub(r"^.+\t"+abc_1+r"([a-z/;-]+)"+abc_2+r"([a-z/;-]+)"+abc_3+r"([a-z/;-]+)"+abc_4+r"([a-z/;-]+)$", r"\4", ii)
      print(abc_1)
      ii=re.sub(r"^([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+([a-z/,.; -]+)[^a-z/,.; -]+\t", r"\1"+hanji_1+r"; \2"+hanji_2+r"; \3"+hanji_3+r"; \4"+hanji_4+r";\t", ii)

    ii=re.sub(r" \t", r"\t",ii)
    l1[index]=ii


  # l1=[re.sub(j1,r' \1, ',ii) for ii in l1]
  # l1=[re.sub(j2,r' \1. ',ii) for ii in l1]
  # l1=[re.sub(r' +',r' ',ii) for ii in l1]
  # l1=[re.sub(r'^ ',r'',ii) for ii in l1]

  # l1=[jaconv.kata2alphabet(ii) for ii in l1]

  # 我們在這個方法中使用 enumerate() 函式。它返回一個列舉物件，該物件也包含計數器和元素。當我們把 enumerate() 函式和 for 迴圈結合起來時，它對 enumerate 物件進行迭代，並把索引和元素一起得到。
  # for index, ii in  enumerate(l1):
  #   ii2=re.sub(r'[,. ]',r'',ii)
  #   if re.match(r"^([a-z]+)[^a-z]+\t\1", ii2):
  #     ii = re.sub(r"^([a-z]+)([^a-z]+)(\t\1)(.+)$",r'\1\2\3 \4;',ii)
  #     l1[index]=ii
      # print(ii)
    # elif re.match(r"^([^a-z]+)([a-z]+)\t.+\2", ii):
    #   ii = re.sub(r"^([^a-z]+)([a-z]+)(\t.+)(\2)$",r'\1\2\3; \4',ii)
    #   l1[index]=ii
    # elif re.match(r"^([a-z]+)([^a-z]+)([a-z]+)\t\1.+\3$", ii):
    #   ii = re.sub(r"^([a-z]+)([^a-z]+)([a-z]+)(\t\1)(.+)(\3)$",r'\1\2\3\4 \5; \6',ii)
    #   l1[index]=ii
    # elif re.match(r"^([^a-z]+)([a-z]+)([^a-z]+)\t.+\2.+$", ii):
    #   ii = re.sub(r"^([^a-z]+)([a-z]+)([^a-z]+)(\t.+)(\2)(.+)$",r'\1\2\3\4; \5 \6;',ii)
    #   l1[index]=ii


  #print(l1)
  strout="\n".join(l1)

  with open("output_jp_split.txt",mode="w",encoding="utf-8") as outfile:
    outfile.write(strout)

  # a=jaconv.kana2alphabet('ら,ー,め,ん,')
  # b=jaconv.kata2alphabet('ケ.ツ.イ.')
  # print(a)
  # print(b)

  # c='シ.リ.ア.ル.らつ通信    shiriarutsuushin;'
  # # c=jaconv.kata2alphabet(c)
  # c=jaconv.kana2alphabet(c)
  # print(c)


if __name__ == "__main__":
  main()
