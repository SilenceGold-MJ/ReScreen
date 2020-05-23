from framework.ReWatermark import WaterMark
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import cv2
from framework.AddQRcode import *
from framework.logger import Logger
logger = Logger(logger="run").getlog()



def ReWater(image_dir):
    for i in os.listdir(image_dir):
        path=image_dir+'\\'+i
        logger.info('图片《%s》,裁剪、去水印、添加新水印、添加二维码，操作完成！！！'%i)
        Screen(path)
        WaterMark().mark(path)
def Screen(file_path):
    sv_path = os.getcwd() + '\\picture_re1\\' + file_path.split('\\')[-1]
    img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), -1)
    sp=(img.shape)#(1080, 1080, 3)=y,x,由三种原色组成


    # 写新水印
    cv2img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # cv2和PIL中颜色的hex码的储存顺序不同
    pilimg = Image.fromarray(cv2img)
    # PIL图片上打印汉字
    draw = ImageDraw.Draw(pilimg)  # 图片上打印#"msyh.ttc""simhei.ttf"
    font = ImageFont.truetype("STHUPO.TTF", 40, encoding="utf-8")  # 参数1：字体文件路径，参数2：字体大小
    draw.text((sp[1]-450, sp[0]-130), "招代理微信：hxxing1", (247, 248, 249),
              font=font)  # 参数1：打印坐标，参数2：文本，参数3：字体颜色，参数4：字体
    # PIL图片转cv2 图片
    cv2charimg = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)
    # cv2.imshow("图片", cv2charimg) # 汉字窗口标题显示乱码

    cropped =cv2charimg[0:sp[1] - 65, 0:sp[0]]  # 裁剪坐标为[y0:y1, x0:x1]
    cv2.imencode('.jpg',  cropped)[1].tofile(sv_path)  # #路径不能为中文解决方法
    AddQRcode(sv_path)

if __name__ =='__main__':
    image_dir=os.getcwd()+'\\picture'
    ReWater(image_dir)
    input('Press Enter to exit...')


