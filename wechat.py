# -*- coding: utf-8 -*-

import base64
from hashlib import md5
import requests
import json
from config import all_config as configs

def wechat_send_msg(body):
    url = configs['wechat']['url']
    headers = {'Content-Type': 'application/json'}
    print("url: %s" % url)
    print("body: %s" % body)
    r = requests.post(url, data=json.dumps(body), headers=headers)
    print(r.text)

def wechat_send_pic_msg(pic_path):
    body = {
        "msgtype": "image",
        "image": {
            "base64": "",
            "md5": "",
        }
    }
    with open(pic_path, 'rb') as f:
        pic = f.read()
        base64_data = base64.b64encode(pic)
        md5_data = md5(pic).hexdigest()
        body["image"]["base64"] = base64_data.decode()
        body["image"]["md5"] = md5_data
    wechat_send_msg(body)

