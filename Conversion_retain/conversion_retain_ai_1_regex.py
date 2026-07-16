# 詢問修改自：conversion_retain_1(完成版).py
import re

# 1. 讀取檔案
with open("input_retain.txt", mode="r", encoding="utf-8") as infile:
    lists = infile.read()

with open("retain_list.txt", mode="r", encoding="utf-8") as inlist:
    retain = eval(inlist.read())  # 讀取的 str 轉換為「列表」

# 2. 將 retain 列表去除重複並排序（長度長的排前面，避免錯殺）
# 原本的 dictWay2 可以直接用內建的 dict.fromkeys 替代，速度更快
retain_unique = sorted(list(dict.fromkeys(retain)), key=len, reverse=True)

# 3. 關鍵加速：將所有保留字組合成一個正規表達式 (例如: "word1|word2|word3")
# 使用 re.escape 可以自動處理保留字中可能含有的特殊符號（如 . * ? 等）
pattern_str = "|".join(re.escape(w) for w in retain_unique)
pattern = re.compile(pattern_str)

# --- 製作 output_retain ---
# 直接用列表推導式比對，且只針對有符合的行放入 result1
listsretain = lists.split('\n')
result1_list = [line for line in listsretain if pattern.search(line)]

# 去除 result1 的重複行並保持順序
result1_unique = list(dict.fromkeys(result1_list))
result1 = "\n".join(result1_unique)

# --- 製作 output_other ---
# 原本的作法是跑幾千次 re.sub，現在改用一條正規表達式直接刪除含有關鍵字的整行
# re.MULTILINE 模式下，^.*(關鍵字).*$\n 可以精準匹配整行並刪除
clean_pattern = re.compile(rf"^.*(?:{pattern_str}).*$(?:\n|$)", re.MULTILINE)
result2 = clean_pattern.sub("", lists)

# 4. 寫入檔案
with open("output_retain.txt", mode="w", encoding="utf-8") as outfile:
    outfile.write(result1)

with open("output_other.txt", mode="w", encoding="utf-8") as outfile:
    outfile.write(result2)
