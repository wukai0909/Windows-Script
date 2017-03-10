# -*- coding: utf-8 -*-
import os, os.path
import shutil
import stat
from PIL import Image

srcpath = r'C:\Users\kai\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'
            

dstpath = r'F:\test'
midpath = r'F:\test1'
dstpath1 = r'F:\test1.1'
dstpath2 = r'F:\test1.2'

#dstpath1 = r'C:\Users\kai\Pictures\windows聚焦'
#dstpath2 = r'C:\Users\kai\Pictures\手机桌面'

def move_file(srcpath, midpath):  # 复制文件
    filelist = os.listdir(srcpath)
    for files in filelist:
        Olddir = os.path.join(srcpath, files);  # 原来的文件路径
        shutil.copy(Olddir, midpath)
    print ('.............move_file............ done')


def rename_file(midpath):  # 重命名文件
    filelist = os.listdir(midpath)
    for files in filelist:
        Olddir = os.path.join(midpath, files);  # 原来的文件路径
        if os.path.isdir(Olddir):  # 如果是文件夹则跳过
            continue;
        filename = os.path.splitext(files)[0];  # 文件名
        # filetype=os.path.splitext(files)[1];#文件扩展名
        Newdir = os.path.join(midpath, filename + ".jpg");  # 新的文件路径
        os.rename(Olddir, Newdir);  # 重命名
        print Newdir
    print ('.............rename_file............ done')


def modify_file_attribute(midpath):  # 修改文件属性
    filelist = os.listdir(midpath)
    for files in filelist:
        Olddir = os.path.join(midpath, files);  # 原来的文件路径
        os.chmod(Olddir, stat.S_IWRITE)  # 修改文件只读属性
    print ('.............modify_file_attribute............ done')


def delete_file_less_200kb(midpath):  # 删除小于200kb的文件
    filelist = os.listdir(midpath)
    for files in filelist:
        Olddir = os.path.join(midpath, files);  # 原来的文件路径
        if os.path.getsize(Olddir) < 200000 :  # 小于200kb且不是JPEG文件 and (im.mode != 'RGB' or im.format != 'JPEG')
             os.remove(Olddir)
             print 'delete',Olddir

    print ('.............delete_less_200kb_file............ done')
	
def delete_file_gif(midpath):  # 删除gif的文件
    filelist = os.listdir(midpath)
    for files in filelist:
        Olddir = os.path.join(midpath, files);  # 原来的文件路径
        im = Image.open(Olddir)
        print files, im.format, im.size, im.mode
        if im.format != 'JPEG' :  # 小于200kb且不是JPEG文件 and (im.mode != 'RGB' or im.format != 'JPEG')
             im.close()
             os.remove(Olddir)
             print 'delete',im.format, im.size, im.mode
        else:
             im.close()

    print ('.............delete_gif_file............ done')
	

def picture_length_width(midpath):  # 判断图片长宽复制到不同的文件路径
    filelist = os.listdir(midpath)
    for files in filelist:
        Olddir = os.path.join(midpath, files);  # 原来的文件路径
        img = Image.open(Olddir)   # img.size 输出 (长, 宽)
        print img
        if img.size[0]>img.size[1]:  # 比较文件长宽
            shutil.copy(Olddir, dstpath1)
        else:
            shutil.copy(Olddir, dstpath2)
    print ('.............picture_length_width............ done')
		

move_file(srcpath, midpath)
rename_file(midpath)
modify_file_attribute(midpath)
delete_file_less_200kb(midpath)
delete_file_gif(midpath)
picture_length_width(midpath)
