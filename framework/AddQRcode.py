from PIL import Image, ImageDraw
import os
from framework.logger import Logger

logger = Logger(logger="AddQRcode").getlog()



def add_watermark_to_image(image, watermark):
    rgba_image = image.convert('RGBA')
    rgba_watermark = watermark.convert('RGBA')

    image_x, image_y = rgba_image.size
    watermark_x, watermark_y = rgba_watermark.size

    # 缩放图片
    scale = 20
    watermark_scale = max(image_x / (scale * watermark_x), image_y / (scale * watermark_y))
    new_size = (int(watermark_x * watermark_scale), int(watermark_y * watermark_scale))
    rgba_watermark = rgba_watermark.resize(new_size, resample=Image.ANTIALIAS)
    # 透明度
    # rgba_watermark_mask = rgba_watermark.convert("L").point(lambda x: min(x,280))
    # rgba_watermark.putalpha(rgba_watermark_mask)

    watermark_x, watermark_y = rgba_watermark.size
    # 水印位置
    rgba_image.paste(rgba_watermark, (image_x - watermark_x-9, image_y - watermark_y-24), rgba_watermark) #右下角
    #rgba_image.paste(rgba_watermark, (image_x - watermark_x, 0), rgba_watermark_mask)  # 右上角

    return rgba_image

def AddQRcode(path):
    im_before = Image.open(str(path))
    im_watermark = Image.open("./framework/mp.jpg")
    im_after = add_watermark_to_image(im_before, im_watermark)
    if  (path.split('.')[0]+".png")==path:
        im_after.save(path, quality=95, subsampling=0)
    else:
        im_after.save(path.split('.')[0] + ".png", quality=95, subsampling=0)
        os.remove(path)

def AddQRcodes():
    for i in os.listdir('./picture_re1'):
        logger.info('图片《%s》,添加二维码完成'%i)
        AddQRcode(os.getcwd()+"\\picture_re1\\" + i)
    for i in os.listdir('./picture_re2'):
        logger.info('图片《%s》,添加二维码完成' % i)
        AddQRcode(os.getcwd() + "\\picture_re2\\" + i)
