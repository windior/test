#判断图片是否为横屏照片并保存
#此版本可以搜索子文件夹
from PIL import Image
import os,shutil
import tkinter as tk
from tkinter import filedialog

import PIL.Image as Image
# 解决 pillow 打开图片大于 20M 的限制
Image.MAX_IMAGE_PIXELS = None

#获取目标工作路径
root=tk.Tk()
root.withdraw()
wd=filedialog.askdirectory()
os.chdir(wd)
print('已成功获取文件夹信息')
if not os.path.exists('D:/new_image'):
    os.mkdir('D:/new_image')
#遍历文件夹
for folder_name, subfolders, filenames in os.walk(wd):
    #print(filenames)
    try:
        for file in filenames:
            f=os.path.join(folder_name,file)
            check_img='.jpg'
            if check_img in f:
                f_img= Image.open(f)
                width,height = f_img.size
                if width/height > 1.5:
                    #复制文件夹中的文件
                    shutil.copy(f,'D:/new_image')
                    print(file+'复制成功')
    except  FileNotFoundError:
                print('发现宝藏')
        
            
