#解压特定rar文件，并保存指定类型文件
import os,shutil,send2trash
from unrar import rarfile
import tkinter as tk
from tkinter import filedialog

def un_rar_file(file_name,path_out,pwd):
    rar_file = rarfile.RarFile(file_name)
    for names in rar_file.namelist():                   # 遍历压缩包内文件名称
        rar_file.extract(names,path_out,pwd)            # 解压文件名、解压后路径、密码
    rar_file._close
#获取目标工作路径
root=tk.Tk()
root.withdraw()
wd=filedialog.askopenfilenames()

print('获取机密文件')

if not os.path.exists('D:/rar'):
    os.mkdir('D:/rar') 
os.chdir('D:/rar')
password=input('输入压缩包密码')
for wd_file in wd:
    if wd_file.endswith('.rar'):
        un_rar_file(wd_file,'D:/rar',password)
        send2trash.send2trash(wd_file)
    if not wd_file.endswith('.rar'):
        wd_rar=wd_file+'.rar'
        os.rename(wd_file,wd_rar) 
        un_rar_file(wd_rar,'D:/rar',password)
        send2trash.send2trash(wd_rar)
    
print('解压中')

for folder_name, subfolders, filenames in os.walk('D:/rar'):
    try:
        for f in filenames:
            if not f.endswith('.rar'):
                f_rar=f+'.rar'
                os.rename(f,f_rar)
            rar=os.path.join(folder_name,f_rar)
            un_rar_file(rar,'D:/rar',password)
    except  FileNotFoundError:
        print('找不到文件')

for folder_name, subfolders, filenames in os.walk('D:/rar'):
    try:
        for rar_file in filenames:
            rar_f=os.path.join(folder_name,rar_file)
            check_file_1='mp4'
            check_file_2='mkv'
            if  rar_f.endswith((check_file_1 , check_file_2),):
                #复制文件夹中的指定文件，以视频为例
                shutil.copy(rar_f,'D:/rar')
                print('复制成功')
    except  FileNotFoundError:
        print('找不到文件')
print('正在灭口')
print('任务完成')

