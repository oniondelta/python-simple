import re


with open("input_main.txt",mode="r",encoding="utf-8") as infile:
    word=infile.read()

with open("conversion_dict.txt",mode="r",encoding="utf-8") as indict:
    change=indict.read()  #讀取的str轉換為字典


def int_change_grave():
    global change #外面來的數需宣告全域變數
    # 轉成所需格式（中間以「@@」作為字典「:」標記）
    change=change.strip()  #刪除空白行
    change=re.sub(r"^",r"{'`", change)
    change=re.sub(r"$",r"`'}", change)
    change=re.sub(r"\n",r"`',\n'`", change)
    change=re.sub(r"@@",r"`':'`", change)


def int_change_direct():
    global change #外面來的數需宣告全域變數
    # 轉成所需格式（中間以「@@」作為字典「:」標記）
    change=change.strip()  #刪除空白行
    change=re.sub(r"^",r"{'", change)
    change=re.sub(r"$",r"'}", change)
    change=re.sub(r"\n",r"',\n'", change)
    change=re.sub(r"@@",r"':'", change)


def change_direct():
    global word #外面來的數需宣告全域變數
    global change #外面來的數需宣告全域變數
    with open("output_conversion_dict.txt",mode="w",encoding="utf-8") as outfile:
        outfile.write(change)

    change=eval(change)  #把字串轉成字典

    #bpmf={"ㄅ":"b","ㄆ":"p","ㄇ":"m","ㄈ":"f","ㄉ":"d","ㄊ":"t","ㄋ":"n","ㄌ":"l","ㄍ":"g","ㄎ":"k","ㄏ":"h","ㄐ":"j","ㄑ":"q","ㄒ":"x"}
    for b in change.keys():
        word=re.sub(b,change[b],word)


def change_repeat_first():
    global word #外面來的數需宣告全域變數
    global change #外面來的數需宣告全域變數
    change=re.sub(r"'`(.+)`':'`",r"'`\1`':'`\1@@",change)
    change_direct()


def change_repeat_first2():
    global word #外面來的數需宣告全域變數
    global change #外面來的數需宣告全域變數
    change=re.sub(r"'(.+)':'",r"'\1':'\1@@",change)
    change_direct()


def remove_grave():
    global word
    word=re.sub(r"`",r"",word)


def to_save():
    with open("output_main.txt",mode="w",encoding="utf-8") as outfile:
        outfile.write(word)


def final_statement():
    print('\n產生：')
    print('轉換字典「output_conversion_dict.txt」')
    print('轉換結果「output_main.txt」')
    print('轉換完成！')


# # int_change() #測試用
# # change_direct() #測試用


def main():
    print('說明：')
    print('《 conversion_dict.txt 中用「@@」等同字典中「:」》')
    print('《 input_main.txt 中，可用「`」限定，例：「`待轉換詞句`」，防止重複替換！》')
    print('《 文檔中注意「`」和「@@」兩個符號，防止誤轉！》\n')

    print('《選項一》：')
    print('1.〔 input_main.txt 中已經使用「`」區分限定待轉換的詞句〕')
    print('2.〔直接替換，可能會重複替換！〕\n')
    select_mode1 = input("請輸入「1」或「2」:")
    select_mode1 = int(select_mode1) #轉換成整數形態

    print('\n《選項二》：')
    print('1.〔 Key 直接替換成 Value 〕')
    print('2.〔 Key 項目接 Value 合在一起替換〕\n')
    select_mode2 = input("請輸入「1」或「2」:")
    select_mode2 = int(select_mode2) #轉換成整數形態

    if select_mode1 == 1 and select_mode2 == 1:
        int_change_grave()
        change_direct()
        remove_grave()
        to_save()
        print('\n注意：原「input_main.txt」和「conversion_dict.txt」，除限定用「`」外，內容不能有「`」，會被移除！')
        final_statement()
    elif select_mode1 == 1 and select_mode2 == 2:
        int_change_grave()
        change_repeat_first()
        remove_grave()
        to_save()
        print('\n注意：原「input_main.txt」和「conversion_dict.txt」，除限定用「`」外，內容不能有「`」，會被移除！')
        final_statement()
    elif select_mode1 == 2 and select_mode2 == 1:
        int_change_direct()
        change_direct()
        to_save()
        final_statement()
    elif select_mode1 == 2 and select_mode2 == 2:
        int_change_direct()
        change_repeat_first2()
        to_save()
        final_statement()
    else:
        print('輸入有誤！')




if __name__ == "__main__":
    main()
