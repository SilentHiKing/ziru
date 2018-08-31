import datetime
import json
import os

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimSun']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False


class ZiruShower:

    # 定义函数来显示柱状上的数值
    def autolabel(self, rects):
        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2. - 0.2, 1.03 * height, '%s' % int(height))

    # 数据显示为图像并保存
    def show_data(self, loc_area_infos, target='ziru'):
        loc = []
        area = []
        total = 0
        for k, v in loc_area_infos.items():
            loc.append(k)
            area.append(v)
            total += v
        # 包含每个柱子下标的序列
        index = np.arange(len(loc))
        # 柱子的宽度
        width = 0.35
        b = plt.bar(index, area, width=width, label='自如房源: %s\n可出租总面积：%d㎡' % (target, total), tick_label=loc, fc='r')
        self.autolabel(b)
        plt.xlabel('城区')
        plt.ylabel('面积（㎡）')
        plt.title('概况')

        # 保存到本地
        abs_path = os.path.dirname(__file__)  # 绝对路径
        path = os.path.join(abs_path, 'pic')
        log = datetime.datetime.now().strftime('%Y-%m-%d')
        # log = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M')
        print('开始储存图片 > %s/%s_%s.jpg' % (path, target, log))
        if os.path.exists(path) is False:
            print('mkdir %s' % path)
            os.mkdir(path)
        plt.legend()  # 显示右上角
        plt.savefig('%s/%s_%s.jpg' % (path, target, log))  # 图片的存储
        print('结束储存图片 > %s/%s_%s.jpg' % (path, target, log))
        plt.show()
        plt.close()

    # 解析数据生成规定的数据形式 如：{'昌平': 总面积}
    def parser_data(self, infos):
        loc_area_infos = {}
        loc_areas = [[info['location'][1][1:3], info['detal'].split('㎡')[0]] for info in infos]
        print('第一次数据整理： ' + str(loc_areas))

        for loc_area in loc_areas:
            k = loc_area[0]
            v = loc_area[1]
            try:
                v = float(v)
            except Exception as e:
                print(e)
                v = v.replace('约', '')
                v = float(v)

            if k in loc_area_infos.keys():
                loc_area_infos[k] = round(loc_area_infos[k] + float(v), 2)
                # print('%s====%d' % (k, loc_area_infos[k]))
            else:
                loc_area_infos[k] = round(float(v), 2)

        print('第二次数据整理: ' + str(loc_area_infos))
        return loc_area_infos

    # 把本地的文档读取生成Python的数据结构
    def get_data(self, path='./data/ziru.txt'):
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
            # print('原始数据： ' + content)
            infos = json.loads(content)
            return infos

    # target 存储图片的名称
    def show(self, infos, target='ziru'):
        print('原始数据： ' + str(infos))
        loc_area_infos = self.parser_data(infos)
        self.show_data(loc_area_infos, target)


if __name__ == '__main__':
    shower = ZiruShower()
    infos = shower.get_data()
    shower.show(infos, '你好')
    # loc_area_infos = show.parser_data(infos)
    # show.show_data(loc_area_infos)
