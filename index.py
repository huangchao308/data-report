#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
from optparse import OptionParser
import os
import shutil
import sys
from excel import excel_catch_screen
from wechat import wechat_send_pic_msg

def main(oss_file_name):
    # TODO 下载 oss 文件
    # TODO 根据 oss 文件生成 excel 文件
    # 截图 Excel
    data_dir = os.path.join(os.path.abspath('.'), 'data')
    date_str = date.today().strftime('%Y%m%d')
    excel_file = os.path.join(data_dir, oss_file_name + date_str + '.xlsx')
    pic_file =  os.path.join(data_dir, oss_file_name + date_str + '.png')
    if os.path.exists(excel_file) is False:
        shutil.copyfile(os.path.join(data_dir, oss_file_name + '.xlsx'), excel_file)
    excel_catch_screen(excel_file, pic_file)
    # 发送微信消息
    wechat_send_pic_msg(pic_file)

if __name__ == '__main__':
    parser = OptionParser(usage='''%prog excel_filename image_filename [options]\nExamples:
            %prog test.xlsx test.png
            %prog test.xlsx test.png -p Sheet2 -r 'A1:C10'
            %prog test.xlsx test.png -r 'B5:C8' ''')
    parser.add_option('-p', '--page', help='pick a page (sheet) by page name. When not specified (and RANGE either not specified or doesn\'t imply a page), first page will be selected')
    parser.add_option('-r', '--range', metavar='RANGE', help='pick a range, in Excel notation. When not specified all used cells on a page will be selected')
    opts, args = parser.parse_args()
    print(opts)
    print(args)

    if len(args) != 2:
        parser.print_help(sys.stderr)
        parser.exit()
    # excel_catch_screen(args[0], args[1], opts.page, opts.range)
    dir = os.path.join(os.path.abspath('.'), 'data')
    if os.path.exists(dir) is False:
        os.mkdir(dir)
    pic_file_path = os.path.join(dir, 'user_data1.png')
    wechat_send_pic_msg(pic_file_path)

# if __name__ == '__main__':
#     parser = OptionParser(usage='''%prog oss_file_name \nExamples:
#             %prog user_data1 ''')
#     opts, args = parser.parse_args()
#     print(opts)
#     print(args)

#     if len(args) != 1:
#         parser.print_help(sys.stderr)
#         parser.exit()
#     main(args[0])
