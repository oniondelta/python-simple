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
from opencc_conversion.iof import IOfile
from opencc_conversion.opencc_c import OpenccConverter

# 設定檔案名稱
input_1="input_opencc_dict.txt"
output_1="output_opencc_dict.txt"

# 設定轉換方式
opencc_json="t2tw.json" #tw2s.json

# 匯入名稱並執行
wc=IOfile.input_file(input_1)

wc=OpenccConverter.run_code(wc, opencc_json)

IOfile.output_file(output_1, wc)

wc=None

# run1=OpenccConverter(input_1,output_1)
# run1.run_code()
