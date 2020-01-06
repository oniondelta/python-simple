

with open("input_bpm.txt",mode="r",encoding="utf-8") as infile:
    word=infile.read()

import re

wc=re.sub(r"([ㄓㄔㄕㄖㄗㄘㄙㄧㄨㄩㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦ])(\s)",r"\1@1\2",word)
wc=re.sub(r"[@][1]|ˉ",r"1",wc)
wc=re.sub(r"ˊ",r"2",wc)
wc=re.sub(r"ˇ",r"3",wc)
wc=re.sub(r"ˋ",r"4",wc)
wc=re.sub(r"˙",r"5",wc)

wc=re.sub(r"ㄌㄩㄢ(\d|\s)",r"lvan\1",wc)
wc=re.sub(r"ㄋㄩㄝ(\d|\s)",r"nve\1",wc)
wc=re.sub(r"ㄌㄩㄝ(\d|\s)",r"lve\1",wc)
wc=re.sub(r"ㄋㄩ(\d|\s)",r"nv\1",wc)
wc=re.sub(r"ㄌㄩ(\d|\s)",r"lv\1",wc)

wc=re.sub(r"ㄅ",r"b",wc)
wc=re.sub(r"ㄆ",r"p",wc)
wc=re.sub(r"ㄇ",r"m",wc)
wc=re.sub(r"ㄈ",r"f",wc)
wc=re.sub(r"ㄉ",r"d",wc)
wc=re.sub(r"ㄊ",r"t",wc)
wc=re.sub(r"ㄋ",r"n",wc)
wc=re.sub(r"ㄌ",r"l",wc)
wc=re.sub(r"ㄍ",r"g",wc)
wc=re.sub(r"ㄎ",r"k",wc)
wc=re.sub(r"ㄏ",r"h",wc)
wc=re.sub(r"ㄐ",r"j",wc)
wc=re.sub(r"ㄑ",r"q",wc)
wc=re.sub(r"ㄒ",r"x",wc)

wc=re.sub(r"ㄓ(\d|\s)",r"zhi\1",wc)
wc=re.sub(r"ㄔ(\d|\s)",r"chi\1",wc)
wc=re.sub(r"ㄕ(\d|\s)",r"shi\1",wc)
wc=re.sub(r"ㄖ(\d|\s)",r"ri\1",wc)
wc=re.sub(r"ㄗ(\d|\s)",r"zi\1",wc)
wc=re.sub(r"ㄘ(\d|\s)",r"ci\1",wc)
wc=re.sub(r"ㄙ(\d|\s)",r"si\1",wc)
wc=re.sub(r"ㄓ",r"zh",wc)
wc=re.sub(r"ㄔ",r"ch",wc)
wc=re.sub(r"ㄕ",r"sh",wc)
wc=re.sub(r"ㄖ",r"r",wc)
wc=re.sub(r"ㄗ",r"z",wc)
wc=re.sub(r"ㄘ",r"c",wc)
wc=re.sub(r"ㄙ",r"s",wc)

wc=re.sub(r"(^|\n|[ \t12345])ㄧㄚ",r"\1ya",wc) #「^」只在文件開頭，一行的開頭為\n
wc=re.sub(r"(^|\n|[ \t12345])ㄧㄛ",r"\1yo",wc)
wc=re.sub(r"(^|\n|[ \t12345])ㄧㄝ",r"\1ye",wc)
wc=re.sub(r"(^|\n|[ \t12345])ㄧㄞ",r"\1yai",wc)
wc=re.sub(r"(^|\n|[ \t12345])ㄧㄠ",r"\1yao",wc)
wc=re.sub(r"(^|\n|[ \t12345])ㄧㄡ",r"\1you",wc)
wc=re.sub(r"(^|\n|[ \t12345])ㄧㄢ",r"\1yan",wc)
wc=re.sub(r"(^|\n|[ \t12345])ㄧㄣ",r"\1yin",wc)
wc=re.sub(r"(^|\n|[ \t12345])ㄧㄤ",r"\1yang",wc)
wc=re.sub(r"(^|\n|[ \t12345])ㄧㄥ",r"\1ying",wc)
wc=re.sub(r"(^|\n|[ \t12345])ㄨㄚ",r"\1wa",wc)
wc=re.sub(r"(^|\n|[ \t12345])ㄨㄛ",r"\1wo",wc)
wc=re.sub(r"(^|\n|[ \t12345])ㄨㄞ",r"\1wai",wc)
wc=re.sub(r"(^|\n|[ \t12345])ㄨㄟ",r"\1wei",wc)
wc=re.sub(r"(^|\n|[ \t12345])ㄨㄢ",r"\1wan",wc)
wc=re.sub(r"(^|\n|[ \t12345])ㄨㄣ",r"\1wen",wc)
wc=re.sub(r"(^|\n|[ \t12345])ㄨㄤ",r"\1wang",wc)
wc=re.sub(r"(^|\n|[ \t12345])ㄨㄥ",r"\1weng",wc)
wc=re.sub(r"(^|\n|[ \t12345])ㄩㄝ",r"\1yue",wc)
wc=re.sub(r"(^|\n|[ \t12345])ㄩㄢ",r"\1yuan",wc)
wc=re.sub(r"(^|\n|[ \t12345])ㄩㄣ",r"\1yun",wc)
wc=re.sub(r"(^|\n|[ \t12345])ㄩㄥ",r"\1yong",wc)

wc=re.sub(r"ㄧㄝ",r"ie",wc)
wc=re.sub(r"ㄧㄡ",r"iu",wc)
wc=re.sub(r"ㄧㄣ",r"in",wc)
wc=re.sub(r"ㄧㄥ",r"ing",wc)
wc=re.sub(r"ㄨㄟ",r"ui",wc)
wc=re.sub(r"ㄨㄣ",r"un",wc)
wc=re.sub(r"ㄨㄥ",r"ong",wc)
wc=re.sub(r"ㄩㄝ",r"ue",wc)
wc=re.sub(r"ㄩㄣ",r"un",wc)
wc=re.sub(r"ㄩㄥ",r"iong",wc)

wc=re.sub(r"(^|\n|[ \t12345])ㄧ([ \t12345])",r"\1yi\2",wc)
wc=re.sub(r"(^|\n|[ \t12345])ㄨ([ \t12345])",r"\1wu\2",wc)
wc=re.sub(r"(^|\n|[ \t12345])ㄩ([ \t12345])",r"\1yu\2",wc)
wc=re.sub(r"ㄧ",r"i",wc)
wc=re.sub(r"ㄨ",r"u",wc)
wc=re.sub(r"ㄩ",r"u",wc)

wc=re.sub(r"ㄚ",r"a",wc)
wc=re.sub(r"ㄛ",r"o",wc)
wc=re.sub(r"ㄜ",r"e",wc)
wc=re.sub(r"ㄝ",r"eh",wc)
wc=re.sub(r"ㄞ",r"ai",wc)
wc=re.sub(r"ㄟ",r"ei",wc)
wc=re.sub(r"ㄠ",r"ao",wc)
wc=re.sub(r"ㄡ",r"ou",wc)
wc=re.sub(r"ㄢ",r"an",wc)
wc=re.sub(r"ㄣ",r"en",wc)
wc=re.sub(r"ㄤ",r"ang",wc)
wc=re.sub(r"ㄥ",r"eng",wc)
wc=re.sub(r"ㄦ",r"er",wc)

wc=re.sub(r"([ \t12345])(5)([a-z]+)",r"\1\3\2",wc) #輕聲在前時換到後面
wc=re.sub(r"51",r"5",wc) #輕聲在前置後時，出現的bug除錯
wc=re.sub(r"(\d)([a-z])",r"\1 \2",wc) #無空格增加空格

#列印與存檔
#print(wc)
with open("output_bpm.txt",mode="w",encoding="utf-8") as outfile:
    outfile.write(wc)

print('''
>> 碼表已由〈注音〉轉換〈拼音〉，檔案：output_bpm.txt''')

# 檢查是否有錯碼
statement='''
《 檢測拼音碼表是否正確 》
 ● 針對〈 RIME 輸入法 terra-pinyin 地球拼音 〉碼表，請先確認以下拼音格式：
① 漢語拼音，「拼音」後須有「聲調」，例：da1 le5。
② ㄋㄩ＝[nv]；ㄌㄩ＝[lv]；ㄋㄩㄝ＝[nve]；ㄌㄩㄝ＝[lve]；ㄌㄩㄢ＝[lvan]，其餘ㄩ＝[u]。
③「字詞」中不可有〈英文〉和〈數字〉。
④ 可保留「＃註解」「詞頻」。
 以下檢測結果：
'''
print(statement)

wc=re.sub(r"[#].*\n",r"\n",wc) #刪除句首井字註解
wc=re.sub(r"\t[0-9\.]+%(\n)",r"\1",wc) #刪除句尾詞頻


pattern=re.compile(r'\d\d|[ \t][ \t]')
search=pattern.search(wc)
if search:
    print(">>《 錯碼！》有〔數字〕〔空格〕重複兩個以上>>",pattern.findall(wc)) #search #.group()
else:
    print("《 正確！》無〔數字〕〔空格〕重複兩個以上")

pattern=re.compile(r'[\s][\d]|\A\d') #|\A\d|(\A|\n)\d
search=pattern.search(wc)
if search:
    print(">>《 錯碼！》有〔數字〕前接〔空格〕〔換行符〕或在行首>>",pattern.findall(wc)) #search #.group()
else:
    print("《 正確！》無〔數字〕前接〔空格〕〔換行符〕或在行首")

pattern=re.compile(r'[a-z]\s|[ \t]\n')
search=pattern.search(wc)
if search:
    print(">>《 錯碼！》有〔英文〕後接〔空格〕〔換行符〕或句尾有〔空格〕>>",pattern.findall(wc)) #search #.group()
else:
    print("《 正確！》無〔英文〕後接〔空格〕〔換行符〕或句尾有〔空格〕")

pattern=re.compile(r'[\d][a-z]')
search=pattern.search(wc)
if search:
    print(">>《 錯碼！》有〔數字〕後接〔英文〕>>",pattern.findall(wc)) #search #.group()
else:
    print("《 正確！》無〔數字〕後接〔英文〕")

pattern=re.compile(r'[^a-z0-9\s][a-z0-9]|[a-z0-9][^a-z0-9\s]')
search=pattern.search(wc)
if search:
    print(">>《 錯碼！》有〔數字〕〔英文〕前後接〔其他字符〕>>",pattern.findall(wc)) #search #.group()
else:
    print("《 正確！》無〔數字〕〔英文〕前後接〔其他字符〕")

#pattern=re.compile(r'[bpmfdtlgkhjqxryw][bpmfdtnlgkhjqxzcsryw]|n[bpmfdtnlkhjqxzcsryw]|[zcs][bpmfdtnlgkjqxzcsryw]|[bpmf][v]|bou|[bpmf]e[hr]|fai|fon|no[abcdefghijklmopqrstvwxyz]|[dt]v|[dtnl]e[hr]|do[abcdefghijklmopqrstvwxyz]|[gk][iv]|[kg]o[abcdefghijklmopqrstvwxyz]|h[v]|[gkh]e[hr]|kei|x[aoe]|[jq][aoe]|[zcsr][h]?[v]|[zcsr][h]?[e][r]|an[abcdefhijklmnopqrstuvwxyz]|ya[abcdefghjklmpqrstuvwxyz]|a[abcdefghjklmpqrstuvwxyz]|ye[ihnr]|e[abcdefgjklmopqstuvwxyz]|yi[euao]|i[bpmfdtlgkhjqxzcsriv]|in[abcdefhijklmnopqrstuvwxyz]|o[bpmfdtlgkhjqxzcsrivaoe]|on[abcdefhijklmnopqrstuvwxyz]|yu[io]|u[bpmfdtlgkhjqxzcsruv]|un[abcdefhijklmnopqrstuvwsyz]|vv|weh|en[abcdefhijklmnopqrstuvwxyz]|w[io][a-z]')
pattern=re.compile(r'[bpmfdtlgkhjqxrvyw][bpmfdtnlgkhjqxzcsryw]|n[bpmfdtnlkhjqxzcsryw]|[zcs][bpmfdtnlgkjqxzcsrywv]|[bpmfdt]v|bou|[bpmf]e[hr]|fai|fon|no[abcdefghijklmopqrstvwxyz]|[dtnl]e[hr]|do[abcdefghijklmopqrstvwxyz]|[gkwv][ivn]|[kg]o[abcdefghijklmopqrstvwxyz]|h[v]|[gkh]e[hr]|x[aoe]|[jq][aoe]|[zcsr][h]?[v]|[zcsr][h]?[e][r]|an[abcdefhijklmnopqrstuvwxyz]|ya[abcdefghjklmpqrstuvwxyz]|a[abcdefghjklmpqrstuvwxyz]|ye[ihnr]|e[abcdefgjklmopqstuvwxyz]|yi[euao]|i[bpmfdtlgkhjqxzcsrivyw]|in[abcdefhijklmnopqrstuvwxyz]|o[bpmfdtlgkhjqxzcsrivaoeyw]|on[abcdefhijklmnopqrstuvwxyz]|yu[io]|u[bpmfdtlgkhjqxzcsruvyw]|un[abcdefhijklmnopqrstuvwsyz]|weh|en[abcdefhijklmnopqrstuvwxyz]|w[io][a-z]')
search=pattern.search(wc)
if search:
    print(">>《 錯碼！》有錯誤的〔拼音〕一（以不正確拼音英文組合檢測）>>",pattern.findall(wc)) #search #.group()
else:
    print("《 正確！》無錯誤的〔拼音〕一（以不正確拼音英文組合檢測）")

#pattern=re.compile(r'[bpmfdtlgkhjqxryiwuvoa][bpmfdtlgkhjqxzcsryw]|[bpmfdtnlgkhjqxzcsrywv][n]|[zsce][bpmfdtlgkjqxzcsywv]|[gkiwvo][i]|[zsc][r]')
#search=pattern.search(wc)
#if search:
#    print("《 錯碼！》有錯誤的〔拼音〕二",search)
#else:
#    print("《 正確！》無錯誤的〔拼音〕二")


wc=re.sub(r"([ \t])r5",r"\1er5",wc) #刪除「兒」(r5)
## 以下特殊拼音，可斟酌遮屏
wc=re.sub(r"fiao4",r"",wc) #（覅 fiao4 ㄈㄧㄠˋ）教育部詞典 特殊發音
wc=re.sub(r"zhei4",r"",wc) #（這 zhei4 ㄓㄟˋ）教育部詞典 特殊發音
#wc=re.sub(r"due3",r"",wc) ###（打了個盹兒 due3 ㄉㄨㄜˇ）教育部詞典 變音發音
wc=re.sub(r"[dt]in4",r"",wc) ###（𨈖 din4 ㄉㄧㄣˋ）（朩 tin4 ㄊㄧㄣˋ）網路詞典 特殊發音
wc=re.sub(r"nui2",r"",wc) #（挼捼 nui2 ㄋㄨㄟˊ）教育部詞典 特殊發音
wc=re.sub(r"nia1",r"",wc) ###（㖸 nia1 ㄋㄧㄚ）網路詞典 特殊發音
wc=re.sub(r"cei4",r"",wc) ###（𤭢 cei4 ㄘㄟˋ）網路詞典 特殊發音
wc=re.sub(r"kei1",r"",wc) ###（剋 kei1 ㄎㄟ）網路詞典 特殊發音
wc=re.sub(r"sei1",r"",wc) #（塞 sei1 ㄙㄟ）教育部詞典 特殊發音
wc=re.sub(r"lo5",r"",wc) #（lo5 ㄌㄛ˙）教育部詞典 特殊發音

## 一般拼音
wc=re.sub(r"[zcs]huang[12345]",r"",wc)
wc=re.sub(r"[zcs]hua[in][12345]",r"",wc)
wc=re.sub(r"[zcs]hang[12345]",r"",wc)
wc=re.sub(r"[zcs]hong[12345]",r"",wc)
wc=re.sub(r"[zcs]hen[g]?[12345]",r"",wc)
wc=re.sub(r"[zcs]hu[aoin][12345]",r"",wc)
wc=re.sub(r"[zcs]hou[12345]",r"",wc)
wc=re.sub(r"[zcs]ha[io][12345]",r"",wc)
wc=re.sub(r"[zcs]han[12345]",r"",wc)
wc=re.sub(r"[s]hei[12345]",r"",wc)
wc=re.sub(r"[zcs]h[auie][12345]",r"",wc)
wc=re.sub(r"[jqx]iong[12345]",r"",wc)
wc=re.sub(r"[dtnljqx]iang[12345]",r"",wc)
wc=re.sub(r"[bpmdtnljqx]ia[on][12345]",r"",wc)
wc=re.sub(r"[bpmdtnljqxy]ing[12345]",r"",wc)
wc=re.sub(r"[pdljqx]ia[12345]",r"",wc) #（pia ㄆㄧㄚ）（dia ㄉㄧㄚ）（lia ㄌㄧㄚ）教育部詞典 變音發音
wc=re.sub(r"[bpmdtnljqxy]ie[12345]",r"",wc)
wc=re.sub(r"[bpmnljqxy]in[12345]",r"",wc)
wc=re.sub(r"[mdnljqx]iu[12345]",r"",wc)
wc=re.sub(r"[bpmdtnljqxrzcsy]i[12345]",r"",wc)
wc=re.sub(r"[gkh]uang[12345]",r"",wc)
wc=re.sub(r"[dtnlgkhjqxrzcsy]uan[12345]",r"",wc)
wc=re.sub(r"[gkh]uai[12345]",r"",wc)
wc=re.sub(r"[gkhzcs]ua[12345]",r"",wc)
wc=re.sub(r"[dtnlgkhxrzcs]uo[12345]",r"",wc)
wc=re.sub(r"[dtnlgkhjqxrzcsy]un[12345]",r"",wc)
wc=re.sub(r"[dtgkhrzcsw]ui[12345]",r"",wc)
wc=re.sub(r"[jqxy]ue[12345]",r"",wc)
wc=re.sub(r"[bpmfdtnlgkhjqxrzcsyw]u[12345]",r"",wc)
wc=re.sub(r"lvan[12345]",r"",wc)
wc=re.sub(r"[nl]v[e]?[12345]",r"",wc)
wc=re.sub(r"[bpmfdtnlgkhwrzcs]?en[g]?[12345]",r"",wc)
wc=re.sub(r"[bpmfdtnlghzw]?ei[12345]",r"",wc)
wc=re.sub(r"e[rh][12345]",r"",wc)
wc=re.sub(r"[mdtnlgkhrzcsy]?e[12345]",r"",wc)
wc=re.sub(r"[bpmfdtnlgkhrzcsyw]?ang[12345]",r"",wc)
wc=re.sub(r"[bpmdtnlgkhzcsyw]?ai[12345]",r"",wc)
wc=re.sub(r"[bpmdtnlgkhrzcsy]?ao[12345]",r"",wc)
wc=re.sub(r"ran[12345]",r"",wc)
wc=re.sub(r"[bpmfdtnlgkhzcsyw]?a[n]?[12345]",r"",wc)
wc=re.sub(r"[dtnlgkhrzcsy]ong[12345]",r"",wc)
wc=re.sub(r"[pmfdtnlgkhrzcsy]?ou[12345]",r"",wc)
wc=re.sub(r"[bpmfyw]?o[12345]",r"",wc)

wc=re.sub(r"[ \t]",r"",wc)
pattern=re.compile(r'[\w]*[a-z0-9]+') #[^a-z0-9\s]
search=pattern.search(wc)
if search:
    print(">>《 錯碼！》有錯誤的〔拼音〕二（刪除所有正確拼法，餘下字元檢測）>>",pattern.findall(wc)) #search #.group()
else:
    print("《 正確！》無錯誤的〔拼音〕二（刪除所有正確拼法，餘下字元檢測）")
