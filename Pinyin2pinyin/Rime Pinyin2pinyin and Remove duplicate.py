
with open("input_pinyin2pinyin.txt",mode="r",encoding="utf-8") as infile:
    word=infile.read()

import re

wc=re.sub(r"([a-zü]*)ī([a-zü]*)",r"\1i\2@",word)
wc=re.sub(r"([a-zü]*)ū([a-zü]*)",r"\1u\2@",wc)
wc=re.sub(r"([a-zü]*)ē([a-zü]*)",r"\1e\2@",wc)
wc=re.sub(r"([a-zü]*)ō([a-zü]*)",r"\1o\2@",wc)
wc=re.sub(r"([a-zü]*)ā([a-zü]*)",r"\1a\2@",wc)

wc=re.sub(r"([a-zü]*)í([a-zü]*)",r"\1i\2@@",wc)
wc=re.sub(r"([a-zü]*)ú([a-zü]*)",r"\1u\2@@",wc)
wc=re.sub(r"([a-zü]*)é([a-zü]*)",r"\1e\2@@",wc)
wc=re.sub(r"([a-zü]*)ó([a-zü]*)",r"\1o\2@@",wc)
wc=re.sub(r"([a-zü]*)á([a-zü]*)",r"\1a\2@@",wc)

wc=re.sub(r"([a-zü]*)ǐ([a-zü]*)",r"\1i\2@@@",wc)
wc=re.sub(r"([a-zü]*)ǔ([a-zü]*)",r"\1u\2@@@",wc)
wc=re.sub(r"([a-zü]*)ě([a-zü]*)",r"\1e\2@@@",wc)
wc=re.sub(r"([a-zü]*)ǒ([a-zü]*)",r"\1o\2@@@",wc)
wc=re.sub(r"([a-zü]*)ǎ([a-zü]*)",r"\1a\2@@@",wc)

wc=re.sub(r"([a-zü]*)ì([a-zü]*)",r"\1i\2@@@@",wc)
wc=re.sub(r"([a-zü]*)ù([a-zü]*)",r"\1u\2@@@@",wc)
wc=re.sub(r"([a-zü]*)è([a-zü]*)",r"\1e\2@@@@",wc)
wc=re.sub(r"([a-zü]*)ò([a-zü]*)",r"\1o\2@@@@",wc)
wc=re.sub(r"([a-zü]*)à([a-zü]*)",r"\1a\2@@@@",wc)

wc=re.sub(r"([a-z]*)ǘ([a-z]*)",r"\1v\2@@",wc)
wc=re.sub(r"([a-z]*)ǚ([a-z]*)",r"\1v\2@@@",wc)
wc=re.sub(r"([a-z]*)ǜ([a-z]*)",r"\1v\2@@@@",wc)

wc=re.sub(r"ü",r"v",wc)

wc=re.sub(r"([a-z]+)(\s)",r"\1@@@@@\2",wc)
wc=re.sub(r"@@@@@",r"5",wc)
wc=re.sub(r"@@@@",r"4",wc)
wc=re.sub(r"@@@",r"3",wc)
wc=re.sub(r"@@",r"2",wc)
wc=re.sub(r"@",r"1",wc)

#print(wc)

# 刪除重複
wc=wc.split('\n') #以\n為分割單元

def dictWay2(wc):
    d = {}
    for i in wc:
        d[i] = None
    return list(d.keys())

wc="\n".join(dictWay2(wc))

# 存檔

with open("output_pinyin2pinyin.txt",mode="w",encoding="utf-8") as outfile:
    outfile.write(wc)

print('''
>> 碼表已由〈拼音 pīn yīn〉轉換〈拼音 pin1 yin1〉，並刪除重複，檔案：output_rime.txt''')

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


pattern=re.compile(r'\d\d|[\t ][\t ]')
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

pattern=re.compile(r'[a-z]\s|[\t ]\n')
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


wc=re.sub(r"([\t ])r5",r"\1er5",wc) #刪除「兒」(r5)
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

wc=re.sub(r"[\t ]",r"",wc)
pattern=re.compile(r'[\w]*[a-z0-9]+') #[^a-z0-9\s]
search=pattern.search(wc)
if search:
    print(">>《 錯碼！》有錯誤的〔拼音〕二（刪除所有正確拼法，餘下字元檢測）>>",pattern.findall(wc)) #search #.group()
else:
    print("《 正確！》無錯誤的〔拼音〕二（刪除所有正確拼法，餘下字元檢測）")
