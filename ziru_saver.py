import os
import json

'''
把数据保存到本地
'''


class ZiruSaver:
    def __init__(self):
        self._datas = []

    def get_datas(self):
        return self._datas

    # 保存数据到数组
    def collect_data(self, data):
        self._datas.extend(data)

    # 把数据保存到文件
    def save_data(self, target='ziru.txt'):
        print('开始储存数据 > %s' % target)
        abs_path = os.path.dirname(__file__)  # 绝对路径
        path = os.path.join(abs_path, 'data')
        if os.path.exists(path) is False:
            print('mkdir %s' % path)
            os.mkdir(path)
        with open('%s/%s' % (path, target), 'w', encoding='utf-8') as file:
            # str = json.dumps(self._datas, ensure_ascii=False, encoding='UTF-8') # 此为转换成字符串
            json.dump(self._datas, file, ensure_ascii=False)  # 存储到本地
        print('储存数据结束 > %s' % target)
