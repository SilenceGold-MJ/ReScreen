# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 16:50
# @Author  :


import cv2 as cv
import numpy as np
import time,os
from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np
from framework.AddQRcode import *



def console_location(path):
    """
    控制台输出区域像素的位置
    :param path:
    :return:
    """
    # 定片位置
    img = cv.imread(path)

    def on_mouse(event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDOWN:
            # 宽 高
            print(x, y)

    # 构建窗口
    # 回调绑定窗口
    cv.namedWindow("img", cv.WINDOW_NORMAL)
    cv.setMouseCallback("img", on_mouse, 0)
    cv.imshow("img", img)
    # 键盘输入 q退出
    if cv.waitKey() == ord("q"):
        cv.destroyAllWindows()


class WaterMark(object):

    def mark(self, path,strs):
        # 提取感兴趣区域ROI
        #img = cv.imread(path)
        img = cv.imdecode(np.fromfile(path, dtype=np.uint8), -1)  # 路径不能为中文解决方法


        # 通过运行console_location函数后在相应的图片上点击两个点可以获取一下两个参数
        # 高1:高2 宽1:宽2
        sp = (img.shape)  # (1080, 1080, 3)=y,x,由三种原色组成

        xx0,yy0=536,55
        xx1,yy1,=16,12
        x0 = int(sp[1] - xx0 - xx1)
        y0 = int(sp[0]-yy0-yy1)
        x1 = int(sp[1]-xx1)
        y1 = int(sp[0] - yy1)

        roi =img[y0:y1,x0:x1]#img[0:sp[1]-65,0:sp[0]]# 高1:高2 宽1:宽2
        # cv.imwrite('02.jpg', roi)
        roi_hsv = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
        # cv.imwrite('hsv.jpg', roi_hsv)

        # 设定白色HSV范围
        # lower = np.array([0,43,46])
        # upper = np.array([13,255,255])
        lower = np.array([0,123,46])
        upper = np.array([180, 255, 255])

        # 创建水印蒙层
        kernel = np.ones((3, 3), np.uint8)
        # cv.imwrite('kernel.jpg',kernel)
        mask = cv.inRange(roi_hsv, lower, upper)
        # cv.imwrite(r'mask.jpg',mask)
        # 对水印蒙层进行膨胀操作
        dilate = cv.dilate(mask, kernel, iterations=3)
        res = cv.inpaint(roi, dilate, 7, flags=cv.INPAINT_TELEA)
        # 双边滤波
        res = cv.bilateralFilter(res, 5, 280, 50)

        # 高1:高2 宽1:宽2
        img[y0:y1,x0:x1]= res

        # # 写新水印
        # font = cv.FONT_HERSHEY_SIMPLEX  # 字体类型: 正常大小无衬线字体
        # # 参数分别是图片, 输入文本数据，放置文本的位置坐标，字体类型，字体大小，颜色为白色，厚度为2
        # cv.putText(img, 'WinXin:hxxing1', (int(x0+(sp[1]-x0)/2)-100, y0+30), font, 1, (247, 248, 249), 3)

        # 写新水印
        cv2img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # cv2和PIL中颜色的hex码的储存顺序不同
        pilimg = Image.fromarray(cv2img)
        # PIL图片上打印汉字
        draw = ImageDraw.Draw(pilimg)  # 图片上打印#"msyh.ttc""simhei.ttf"
        font = ImageFont.truetype("STHUPO.TTF", 40, encoding="utf-8")  # 参数1：字体文件路径，参数2：字体大小
        draw.text((sp[1] - int(sp[1] * 480 / sp[1]), (y0+10)), strs, (192, 74, 64),font=font)  # 参数1：打印坐标，参数2：文本，参数3：字体颜色，参数4：字体

        #draw.text((int(x0+(sp[1]-x0)/2)-185, y0+10),strs, (192, 74, 64), font=font)  # 参数1：打印坐标，参数2：文本，参数3：字体颜色，参数4：字体
        # PIL图片转cv2 图片
        cv2charimg = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)
        # cv2.imshow("图片", cv2charimg) # 汉字窗口标题显示乱码

        #now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        image_dir = os.getcwd() + '\\picture_re2\\'+path.split('\\')[-1]
        #cv.imwrite(image_dir, img)
        cv.imencode('.jpg', cv2charimg)[1].tofile(image_dir)  # 路径不能为中文解决方法
        AddQRcode(image_dir)



# if __name__ == '__main__':
#     path = '20200518122417.jpg'
#     # console_location(path)
#     w = WaterMark()
#     w.mark(path)


