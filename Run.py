
from framework.AddQRcode import *
import platform
from framework.logger import Logger
import configparser,os
proDir = os.getcwd()
configPath = os.path.join(proDir, "config\config.ini")
cf = configparser.ConfigParser()
cf.read(configPath,encoding="utf-8-sig")

logger = Logger(logger="run").getlog()



def ReWater(strs,fon_stra,image_dir,fon_path_win7,fon_path_win10):

    fon_path = fon_path_win7 if platform.platform().split('-') [1]=='7' else  fon_path_win10
    for i in os.listdir(image_dir):
        path=image_dir+'\\'+i
        logger.info('图片《%s》,添加水印、添加二维码，操作完成！！！'%i)
        AddQRcode(path, strs,fon_stra,fon_path)


if __name__ =='__main__':
    image_dir=os.getcwd()+'\\picture'
    fon_stra=int(cf.get("Data", "fon_stra"))# 水印字体大小
    strs=cf.get("Data", "ShuiYin")  #水印内容
    fon_path_win10=r"C:\Windows\Fonts\%s"%cf.get("Data", "fon_win10")#  win10系统水印字体
    fon_path_win7 = r"C:\Windows\Fonts\%s"%cf.get("Data", "fon_win7")  #win7系统 水印字体
    ReWater(strs,fon_stra,image_dir,fon_path_win7,fon_path_win10)
    input('Press Enter to exit...')


