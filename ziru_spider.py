from util.downloader import DownLoader
from ziru_parser import ZiruParser
from ziru_saver import ZiruSaver
from ziru_shower import ZiruShower
from util.util import run_time


class ZiruSpider:

    def __init__(self):
        self.loader = DownLoader()
        self.parser = ZiruParser()
        self.saver = ZiruSaver()
        self.shower = ZiruShower()
        self.count = 0
        self.depth = float('inf')

    def crawl(self, url):
        if self.count >= self.depth:
            return
        self.count = self.count + 1
        print('%d ========== %s' % (self.count, url))
        content = self.loader.download(url)
        urls, datas = self.parser.parse(url, content)
        if datas:
            self.saver.collect_data(datas)
        if urls:
            url = urls.pop()
            self.crawl(url)

    @run_time
    def start(self, url, target='ziru.txt', depth=float('inf')):
        self.depth = depth
        self.parser.set_main_url('http://')
        self.crawl(url)
        self.saver.save_data(target=target)
        self.show_datas(target.split('.')[0])

    # 展示从网络获取的数据
    # pic_name 图片的名称
    def show_datas(self, pic_name=''):
        datas = self.saver.get_datas()
        self.shower.show(datas, target=pic_name)


if __name__ == '__main__':
    spider = ZiruSpider()
    spider.start('http://www.ziroom.com/z/nl/z3.html')
