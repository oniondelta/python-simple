import numpy as np
# import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
# import statistics

with open("in_number.txt",mode="r",encoding="utf-8") as infile:
    list_x=infile.read()

list_x=list_x.split('\n') #以\n為分割單元
list_x=list(map(int,list_x)) # list 中單元原為 string 轉成數值整數（int）
# list_x = np.random.normal(size=100)
# print(x)


# 對 list_x 進行運算
list_x[:] = [a - 5468 for a in list_x]
list_x[:] = [round((b*abs(b)/1000)*1.2) for b in list_x]    # round() 四捨五入    #abs()絕對值



list_x2 = (str(c) for c in list_x)    # 變成string才能使用.join
strout="\n".join(list_x2)

with open("out_number.txt",mode="w",encoding="utf-8") as outfile:
    outfile.write(strout)


print("中位數：", np.median(list_x))
print("平均數：", np.mean(list_x))
print("最大數：", np.max(list_x))
print("最小數：", np.min(list_x))
# print("標準差：", np.std(list_x))
print("標準差(分母(n)，有偏估計)：", np.std(list_x, ddof=0))    # 分母(n)，有偏估計
print("標準差(分母(n-1)，無偏估計)：", np.std(list_x, ddof=1))    # 分母(n-1)，無偏估計

sns.displot(list_x, bins=100, kde=False)    # bins分幾格    # kde 只顯示直方圖之趨勢與否
plt.show()


