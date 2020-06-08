
from framework.AddQRcode import *
from framework.logger import Logger
logger = Logger(logger="run").getlog()



def ReWater(strs,fon_stra,image_dir,fon_path):
    for i in os.listdir(image_dir):
        path=image_dir+'\\'+i
        logger.info('图片《%s》,添加水印、添加二维码，操作完成！！！'%i)
        AddQRcode(path, strs,fon_stra,fon_path)


if __name__ =='__main__':
    image_dir=os.getcwd()+'\\picture'
    fon_stra=25# 水印字体大小
    strs='诚招代理'  #水印内容
    fon_path=r"C:\Windows\Fonts\STHUPO.TTF"#  水印字体
    ReWater(strs,fon_stra,image_dir,fon_path)
    input('Press Enter to exit...')


