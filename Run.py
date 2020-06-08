
from framework.AddQRcode import *
import platform
from framework.logger import Logger
logger = Logger(logger="run").getlog()



def ReWater(strs,fon_stra,image_dir,fon_path_win7,fon_path_win10):

    fon_path = fon_path_win7 if platform.platform().split('-') [1]=='7' else  fon_path_win10
    for i in os.listdir(image_dir):
        path=image_dir+'\\'+i
        logger.info('图片《%s》,添加水印、添加二维码，操作完成！！！'%i)
        AddQRcode(path, strs,fon_stra,fon_path)


if __name__ =='__main__':
    image_dir=os.getcwd()+'\\picture'
    fon_stra=25# 水印字体大小
    strs='诚招代理'  #水印内容
    fon_path_win10=r"C:\Windows\Fonts\STHUPO.TTF"#  win10系统水印字体
    fon_path_win7 = r"C:\Windows\Fonts\方正粗黑宋简体.ttf"  #win7系统 水印字体
    ReWater(strs,fon_stra,image_dir,fon_path_win7,fon_path_win10)
    input('Press Enter to exit...')


