#windior 
#找出目标文件并存放于指定位置
#此版本可以搜索子文件夹

import os,shutil
import tkinter as tk
from tkinter import filedialog

#获取目标工作路径
root=tk.Tk()
root.withdraw()
wd=filedialog.askdirectory()
os.chdir(wd)
print('已成功获取文件夹信息')

#指定目标文件格式
check_file=input('输入要查询的文件名or文件类型: ')
print('已指定文件信息')


#选择存放的文件夹
target_root=tk.Tk()
target_root.withdraw()
tar_wd=filedialog.askdirectory()
print('已指定文件夹')

#遍历文件夹
for folder_name, subfolders, filenames in os.walk(wd):
    #print(filenames)
    try:
        for file in filenames:
            f=os.path.join(folder_name,file)
            if check_file in f:
                #复制文件夹中的文件
                shutil.copy(f,tar_wd)
                print(file+'复制成功')
    except  FileNotFoundError:
        print('找不到文件')

print('任务完成')
        
            
