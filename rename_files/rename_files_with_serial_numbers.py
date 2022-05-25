import os
import shutil
import re


def run_rename_sn():
    # 獲取該目錄下所有檔案，存入列表中
    path_o = "./original_files/"
    f_o = os.listdir(path_o)
    print("資料夾包含：" ,len(f_o) ,"個檔案")
    # print("測試檔名擷取：" ,f[0])

    file_extension = '.jpg'

    check_ok = False
    for i in f_o:
        i = re.sub(file_extension+r'$', "", i)
        # i = re.sub(r"\.jpg$", "", i)
        # print(i)
        if i.isdigit() == True:
            check_ok = True
    # print("檢驗是否有全數字檔名：" ,check_ok)

    if check_ok == False:
        # 保險起見，檔案複製到新資料夾再作重命名修改
        shutil.copytree('./original_files/', './rename_files/')

        # 獲取該目錄下所有檔案，存入列表中
        path_r = "./rename_files/"
        f_r = os.listdir(path_r)

        print("修改檔名開始：")
        n = 0
        for i in f_r:
            # 設定舊檔名
            old_name = f_r[n]
            # 設定新檔名
            new_name = str(n+1) + file_extension
            # 用os模組中的rename方法對檔案改名（路徑+檔名）
            os.rename(path_r+old_name, path_r+new_name)
            print(old_name, '======>', new_name)
            n += 1
    else:
        print("檔名包含全數字，會掉檔案，故不作處理！！！")


def main():
    # 檢查資料夾是否存在
    folder_path = "./rename_files/"
    result = os.path.isdir(folder_path)
    # print(result)

    if result == False:
        run_rename_sn()

    else:
        print("「rename_files」資料夾已經存在")




if __name__ == "__main__":
    main()