import os
import json

'''
把数据保存到本地
'''


class ZiruAllSaver:
    def __init__(self):
        self.datas = []

    # 保存数据到数组
    def collect_data(self, data):
        self.datas.extend(data)
