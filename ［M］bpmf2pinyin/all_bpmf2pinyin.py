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
from bp2py_modules.iof import IOfile
from bp2py_modules.bp2py import Bpmf2Pinyin
# from bp2py_modules.bp2py_old import Bpmf2PinyinOld
from bp2py_modules.rd5 import RemoveDuplicate5
from bp2py_modules.ckpy import CheckPinyin

# # 原設定檔案名稱
# input_1="input_pinyin2pinyin.txt"
# output_1="output_pinyin2pinyin.txt"
# output_2="output_pinyin2pinyin.txt"
# 設定檔案名稱
input_1="input_bpmf.txt"
output_1="ok_bp2py.txt"
output_2="output_finish-bp2py_rd5.txt"

# 匯入名稱並執行
wc=IOfile.input_file(input_1)

wc=Bpmf2Pinyin.run_code(wc)
IOfile.output_file(output_1,wc)

# wc=Bpmf2PinyinOld.run_code(wc)
# IOfile.output_file(output_1,wc)

# wc=RemoveDuplicate5.run_code(wc)
# IOfile.output_file(output_2,wc)

CheckPinyin.run_code(wc)
wc=None
# print(wc)

# run1=Bpmf2Pinyin(input_1,output_1)
# run1=Bpmf2PinyinOld(input_1,output_1)
# run2=RemoveDuplicate5(output_1,output_2)
# run3=CheckPinyin(output_2)
# run1.run_code()
# run2.run_code()
# run3.run_code()
# # wc=run1.run_code()
# # print(wc)
# # run3=CheckPinyin(run1.run_code())
# # CheckPinyin.run_code(wc)
