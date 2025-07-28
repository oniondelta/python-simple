#主程式
#成功載入封包中的模組
# import pp12_package.pp12_point #點的前為資料夾名稱（封包名稱），後面為裡面的模組檔案名稱
# result=pp12_package.pp12_point.distance(3,4)
# print("距離：",result)

# import pp12_package.pp12_line
# result=pp12_package.pp12_line.slope(1,1,3,3)
# print("斜率：",result)

# import pp12_package.pp12_line as line #路徑太長，轉換替代名稱，後續都須用該替代名稱
# result=line.slope(1,2,4,3)
# print("斜率：",result)


# 使用模組 module
from rd5_and_sort2_modules.iof import IOfile
from rd5_and_sort2_modules.rd5 import RemoveDuplicate5
from rd5_and_sort2_modules.sort2 import SortByWordCount2

# 設定檔案名稱
input_1="input_dict.txt"
output_1="rd_ok.txt"
output_2="output_finish.txt"

# 匯入名稱並執行
wc=IOfile.input_file(input_1)

wc=RemoveDuplicate5.run_code(wc)
IOfile.output_file(output_1,wc)

wc=SortByWordCount2.run_code(wc)
IOfile.output_file(output_2,wc)

wc=None

# run1=RemoveDuplicate5(input_1,output_1)
# run2=SortByWordCount2(output_1,output_2)
# run1.run_code()
# run2.run_code()
