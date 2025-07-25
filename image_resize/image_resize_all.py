### 小於 max 尺寸的也會放大

import os
import glob
from PIL import Image


max = 720                    # 設定長或寬最大的數值


def img_resize():
    imgs = glob.glob('./resize_in/*.jpg')
    for i in imgs:
        im = Image.open(i)
        size = im.size               # width=size[0], height=size[1]
        # print(size)
        if size[0]>size[1]:          # 如果原始圖片 width 大於 height
            scale = size[1]/size[0]  # 設定 scale 為 height/width
            w = max                  # 設定調整後的寬度為最大的數值
            h = int(max*scale)       # 設定調整後的高度為 max 乘以 scale ( 使用 int 去除小數點 )
        else:                        # 如果原始圖片 width 小於等於 height
            scale = size[0]/size[1]  # 設定 scale 為 width/height
            w = int(max*scale)       # 設定調整後的寬度為 max 乘以 scale ( 使用 int 去除小數點 )
            h = max                  # 設定調整後的高度為最大的數值
        name = i.split('/')[::-1][0]
        im2 = im.resize((w, h))      # 調整尺寸
        im2.save(f'./resize_all_out/{name}')


class main():
    # 檢查資料夾是否存在
    folder_path = "./resize_all_out/"
    result = os.path.isdir(folder_path)
    # print(result)
    if result == False:
        # 建立資料夾
        os.mkdir("./resize_all_out/")
        img_resize()
    else:
        print("「resize_all_out」資料夾已經存在\n！！！終止執行！！！")


if __name__ == "__main__":
    main()
