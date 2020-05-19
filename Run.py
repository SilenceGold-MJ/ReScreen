from framework.ReWatermark import WaterMark
import numpy as np
from framework.logger import Logger

logger = Logger(logger="run").getlog()
import cv2,os,time
def ReWater(image_dir):
    for i in os.listdir(image_dir):
        path=image_dir+'\\'+i
        logger.info('图片《%s》,裁剪、去水印完成'%i)
        Screen(path)
        WaterMark().mark(path)
def Screen(file_path):
    sv_path = os.getcwd() + '\\picture_re1\\' + file_path.split('\\')[-1]
    img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), -1)
    sp=(img.shape)#(1080, 1080, 3)=y,x,由三种原色组成

    cropped = img[0:sp[1]-65,0:sp[0]] # 裁剪坐标为[y0:y1, x0:x1]
    cv2.imencode('.jpg',  cropped)[1].tofile(sv_path)  # #路径不能为中文解决方法

if __name__ =='__main__':
    image_dir=os.getcwd()+'\\picture'
    ReWater(image_dir)
    input('Press Enter to exit...')


