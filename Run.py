
from framework.AddQRcode import *
import platform
import imghdr
from framework.logger import Logger
import configparser,os
proDir = os.getcwd()
configPath = os.path.join(proDir, "config\config.ini")
cf = configparser.ConfigParser()
cf.read(configPath,encoding="utf-8-sig")

logger = Logger(logger="run").getlog()

def Getimage(rootdir):#所有文件列表
    _files = []
    dirs=[]
    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])  # 合并路径，将rootdir和list合并
        if os.path.isdir(path):
            _files.extend(Getimage(path)[0]) # 递归调用函数
            dirs.extend(Getimage(path)[1])
        if os.path.isfile(path):
            if imghdr.what(path) in ["bmp", "jpg", "png", "gif", "jpeg"]:
                _files.append(path)
                dirs.append(int(path.split('\\')[-2]))

    return [_files,dirs]

def ReWater(strs,fon_stra,image_dir,fon_path_win7,fon_path_win10):

    fon_path = fon_path_win7 if platform.platform().split('-') [1]=='7' else  fon_path_win10
    filelist=Getimage(image_dir)[0]
    #logger.info(filelist)
    for i in filelist:

        logger.info('图片《%s》,添加水印、添加二维码，操作完成！！！'%i.split('\\')[-1])
        AddQRcode(i, strs,fon_stra,fon_path)


if __name__ =='__main__':
    image_dir=os.getcwd()+'\\picture'
    fon_stra=int(cf.get("Data", "fon_stra"))# 水印字体大小
    strs=cf.get("Data", "ShuiYin")  #水印内容
    fon_path_win10=r"C:\Windows\Fonts\%s"%cf.get("Data", "fon_win10")#  win10系统水印字体
    fon_path_win7 = r"C:\Windows\Fonts\%s"%cf.get("Data", "fon_win7")  #win7系统 水印字体
    ReWater(strs,fon_stra,image_dir,fon_path_win7,fon_path_win10)
    input('Press Enter to exit...')


