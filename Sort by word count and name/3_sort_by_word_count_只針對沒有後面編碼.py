with open("input_sort_count.txt",mode="r",encoding="utf-8") as infile:
    word=infile.read()

listword=word.split('\n') # list化

listword=sorted(listword, key=len)

listword="\n".join(listword) # 轉成字串（string）形式

with open("output_3_sort_count.txt",mode="w",encoding="utf-8") as outfile:
    outfile.write(listword)