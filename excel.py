# -*- coding: utf-8 -*-

import os
from PIL import ImageGrab
import xlwings as xw

# get_screenshot
def excel_catch_screen(excel_file, pic_file, excel_sheet_name='Sheet1', excel_range=''):
    # 使用xlwings的app启动
    app = xw.App(visible=True,  add_book=False)    
    # 打开文件
    wb = app.books.open(excel_file)    
    # 选定sheet
    sheet = wb.sheets(excel_sheet_name)    
    if excel_range:
        all = sheet.range(excel_range) # 获取指定范围的 range
    else:
        all = sheet.used_range # 获取有内容的 range
    # 复制图片区域
    all.api.copy_picture()

    # 获取剪贴板的图片数据
    img = ImageGrab.grabclipboard()
    dir = os.path.join(os.path.abspath('.'), 'data')
    if os.path.exists(dir) is False:
        os.mkdir(dir)
    pic_file_path = os.path.join(dir, pic_file + '.png')
    img.save(pic_file_path)    # 保存图片
    wb.close()    # 不保存，直接关闭
    app.quit()
