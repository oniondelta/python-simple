# 詢問修改自：ai_1版

# 1. 讀取檔案
with open("input_retain.txt", mode="r", encoding="utf-8") as infile:
    lists = infile.read()

with open("retain_list.txt", mode="r", encoding="utf-8") as inlist:
    # 讀取的 str 轉換為「列表」，並直接用 dict.fromkeys 去除重複值
    retain = list(dict.fromkeys(eval(inlist.read())))

listsretain = lists.split('\n')

# 2. 核心加速：使用內建的 any() 與 in 進行純文字比對
# 只要行(line)裡面包含 retain 中的任意一個字，就保留
result1_list = [
    line for line in listsretain 
    if any(keyword in line for keyword in retain)
]

# 去除 result1_list 的重複行並保持順序，最後結合成字串
result1 = "\n".join(dict.fromkeys(result1_list))

# 3. 核心加速：製作 output_other
# 只要行(line)裡面「沒有」包含 retain 中的任何一個字，就留下來
result2_list = [
    line for line in listsretain 
    if not any(keyword in line for keyword in retain)
]
result2 = "\n".join(result2_list)

# 4. 寫入檔案
with open("output_retain.txt", mode="w", encoding="utf-8") as outfile:
    outfile.write(result1)

with open("output_other.txt", mode="w", encoding="utf-8") as outfile:
    outfile.write(result2)
