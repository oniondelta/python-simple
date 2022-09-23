### 小於 max 尺寸的不放大

import os
import glob
import shutil
from PIL import Image


max = 1080                    # 設定長或寬最大的數值


def imgresize(max,size,im,name):
    if size[0]>size[1]:          # 如果原始圖片 width 大於 height
        scale = size[1]/size[0]  # 設定 scale 為 height/width
        w = max                  # 設定調整後的寬度為最大的數值
        h = int(max*scale)       # 設定調整後的高度為 max 乘以 scale ( 使用 int 去除小數點 )
    else:                        # 如果原始圖片 width 小於等於 height
        scale = size[0]/size[1]  # 設定 scale 為 width/height
        w = int(max*scale)       # 設定調整後的寬度為 max 乘以 scale ( 使用 int 去除小數點 )
        h = max                  # 設定調整後的高度為最大的數值
    im2 = im.resize((w, h))      # 調整尺寸
    # im2 = im.resize((w, h), Image.Resampling.BICUBIC)      # 調整尺寸
    # im2 = im.resize((w, h), Image.Resampling.NEAREST)      # 調整尺寸
    # im2 = im.resize((w, h), Image.Resampling.BILINEAR)      # 調整尺寸
    # im2 = im.resize((w, h), Image.Resampling.LANCZOS)      # 調整尺寸
    im2.save(f'./resize_max_out/{name}')

def checksize():
    imgs = glob.glob('./resize_in/*.jpg')
    for i in imgs:
        name = i.split('/')[::-1][0]
        im = Image.open(i)
        size = im.size           # width=size[0], height=size[1]
        # print(size)
        if size[0]>max:
            imgresize(max,size,im,name)
        elif size[1]>max:
            imgresize(max,size,im,name)
        else:
            im.save(f'./resize_max_out_i/{name}')  # 因解譯後另存，尺寸不變，但會改變檔案容量大小（畫質清晰度會變差）！
            # im.save(f'./resize_max_out_i/{name}', quality=85)  # 因解譯後另存，尺寸不變，但會改變檔案容量大小（畫質清晰度會變差）！
            # im.save(f'./resize_max_out_i/{name}',quality=80, subsampling=0)  # 因解譯後另存，尺寸不變，但會改變檔案容量大小（畫質清晰度會變差）！
            shutil.copyfile(f"./resize_in/{name}", f"./resize_max_out_o/{name}")  # 直接複製過去，尺寸和檔案容量大小不變！

class main():
    # 檢查資料夾是否存在
    folder_path = "./resize_max_out/"
    folder_path1 = "./resize_max_out_o/"
    folder_path2 = "./resize_max_out_i/"
    result = os.path.isdir(folder_path)
    result1 = os.path.isdir(folder_path1)
    result2 = os.path.isdir(folder_path2)
    # print(result)
    # if result == False:
    #     # 建立資料夾
    #     os.mkdir("./resize_max_out/")
    #     checksize()
    if result == False and result1 == False and result2 == False:
        # 建立資料夾
        os.mkdir("./resize_max_out/")
        os.mkdir("./resize_max_out_o/")
        os.mkdir("./resize_max_out_i/")
        checksize()
        print("完成！")
        print("「resize_max_out」有縮減尺寸之圖檔")
        print("「resize_max_out_o」無縮減尺寸之圖檔：直接原檔複製，檔案容量畫質不變！")
        print("「resize_max_out_i」無縮減尺寸之圖檔：因解譯另存，檔案容量變小，畫質變差！")
    else:
        print("「resize_max_out」三個資料夾之一已存在\n！！！終止執行！！！")


if __name__ == "__main__":
    main()

