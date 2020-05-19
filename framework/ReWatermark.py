# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 16:50
# @Author  :


import cv2 as cv
import numpy as np
import time,os


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

    def mark(self, path):
        # 提取感兴趣区域ROI
        img = cv.imread(path)
        # 通过运行console_location函数后在相应的图片上点击两个点可以获取一下两个参数
        # 高1:高2 宽1:宽2
        sp = (img.shape)  # (1080, 1080, 3)=y,x,由三种原色组成
        bzy0 = 1010 / 1080
        bzy1 = 1060 / 1080
        bzx0 = 530 / 1080
        bzx1 = 1060 / 1080
        y0 = int(sp[0] * bzy0)
        y1 = int(sp[0] * bzy1)
        x0 = int(sp[1] * bzx0)
        x1 = int(sp[1] * bzx1)

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
        #now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        image_dir = os.getcwd() + '\\picture_re2\\'+path.split('\\')[-1]
        cv.imwrite(image_dir, img)


# if __name__ == '__main__':
#     path = '20200518122417.jpg'
#     # console_location(path)
#     w = WaterMark()
#     w.mark(path)


