from PIL import Image, ImageDraw
from PIL import Image, ImageDraw, ImageFont
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import os
import configparser,os
proDir = os.getcwd()
configPath = os.path.join(proDir, "config\config.ini")
cf = configparser.ConfigParser()
cf.read(configPath,encoding="utf-8-sig")

from framework.logger import Logger

logger = Logger(logger="AddQRcode").getlog()



def add_watermark_to_image(image, watermark,strs,fon_stra,fon_path):
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

    #print(( (image_x - watermark_x-9, image_y - watermark_y-20)))
    rgba_image.paste(rgba_watermark, (image_x - watermark_x-9, image_y - watermark_y-20), rgba_watermark) #右下角
    #rgba_image.paste(rgba_watermark, (image_x - watermark_x, 0), rgba_watermark_mask)  # 右上角

    draw = ImageDraw.Draw(rgba_image)  # 图片上打印#"msyh.ttc""simhei.ttf"

    fon = int(watermark_y * (fon_stra / 63))
    # print(fon,sp[0],int(40/1200))
    font = ImageFont.truetype(fon_path, fon, encoding="utf-8")  # 参数1：字体文件路径，参数2：字体大小
    draw.text((( image_x - watermark_x-9- int((len(strs.encode('utf-8')) - len(strs)) / 2 + len(strs)) * fon/2 ), image_y - fon-20), strs, (192, 74, 64),
              font=font)  # 参数1：打印坐标，参数2：文本，参数3：字体颜色，参数4：字体
    # PIL图片转cv2 图片


    return rgba_image

def AddQRcode(path,strs,fon_stra,fon_path):

    if not os.path.exists(os.getcwd() + '\\picture_re3\\'):
        os.makedirs(os.getcwd() + '\\picture_re3\\')
    sv_path = os.getcwd() + '\\picture_re3\\' + path.split('\\')[-1]
    im_before = Image.open(str(path))
    im_watermark = Image.open("./config/%s"%cf.get("Data", "ErWeiMa"))
    im_after = add_watermark_to_image(im_before, im_watermark,strs,fon_stra,fon_path)
    #im_after.save(sv_path, quality=95, subsampling=0)
    captcha =im_after.convert('RGB')
    captcha.save(sv_path)
