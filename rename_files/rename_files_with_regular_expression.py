import os
import shutil
import re


def run_rename_re():
    # 獲取該目錄下所有檔案，存入列表中
    path_o = "./original_files/"
    f_o = os.listdir(path_o)
    print("轉換前資料夾包含：" ,len(f_o) ,"個檔案")
    # print("測試檔名擷取：" ,f_o[0])

    # 獲取該目錄下所有檔案，存入列表中
    path_r = "./rename_files_re/"
    f_r = os.listdir(path_r)
    # print("測試檔名擷取：" ,f_r[0])

####################################################################
# 正則替換修改處(會有問題！)：
# input_pattern = '(CST_)(.+)_(\d+)(\.)'
# rename_pattern = '\1\3\2\4'
####################################################################
    print("《修改檔名開始》：")
    for old_name in f_r:
        # 正則修改檔名
        # new_name = re.sub(input_pattern, rename_pattern, old_name)
        # new_name = re.sub(input_pattern, r'\1\3_\2\4', old_name)
        new_name = re.sub(r'(CST_)(.+)_(\d+)(\.)', r'\1\3_\2\4', old_name)

        # 用os模組中的rename方法對檔案改名（路徑+檔名）
        os.rename(path_r+old_name, path_r+new_name)

        print(old_name, '======>', new_name)
    # print("轉換後資料夾包含：" ,len(f_r) ,"個檔案")


def main():
    # 檢查資料夾是否存在
    folder_path = "./rename_files_re/"
    result = os.path.isdir(folder_path)
    # print(result)

    if result == False:
        # 保險起見，檔案複製到新資料夾再作重命名修改
        shutil.copytree('./original_files/', './rename_files_re/')
        run_rename_re()

    else:
        print("「rename_files_re」資料夾已經存在")




if __name__ == "__main__":
    main()




# check_ok = False
# for i in f:
#     i = re.sub(r"\.jpg$", "", i)
#     # print(i)
#     if i.isdigit() == True:
#         check_ok = True
# # print("檢驗是否有全數字檔名：" ,check_ok)


# if check_ok == False:
#     print("修改檔名開始：")
#     n = 0
#     for i in f:
#         # 設定舊檔名
#         oldname = f[n]
#         # 設定新檔名
#         newname = str(n+1) + '.jpg'
#         # 用os模組中的rename方法對檔案改名（路徑+檔名）
#         os.rename(path+oldname, path+newname)
#         print(oldname, '======>', newname)
#         n += 1
# else:
#     print("檔名包含全數字，不作處理！！！")


