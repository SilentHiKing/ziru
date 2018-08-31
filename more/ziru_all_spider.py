import os
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Pool

from util.downloader import DownLoader
from ziru_spider import ZiruSpider
from more.ziru_all_parser import ZiruAllParser
from more.ziru_all_saver import ZiruAllSaver



class ZiruAllSpider:

    def __init__(self):
        self.loader = DownLoader()
        self.parser = ZiruAllParser()
        self.saver = ZiruAllSaver()

        self.pool = Pool(os.cpu_count())
        self.process_pool = ProcessPoolExecutor()

    def crawl(self, url):
        print('========== %s' % url)
        content = self.loader.download(url)
        datas = self.parser.parse(url, content)
        if datas:
            self.saver.collect_data(datas)

    def start(self, url, depth=float('inf'), target='ziru.txt'):
        self.crawl(url)
        infos = self.saver.datas
        print(infos)
        for info in infos:
            url = info[0]
            city = info[1]
            print(' >>>>>>> %s' % str(info))
            # self.city_spider(url, city)
            self.pool.apply_async(ZiruAllSpider.city_spider, args=(url, city))
        print('Waiting for all subprocesses done...')
        self.pool.close()
        self.pool.join()
        print('All subprocesses done.')

    def city_spider(url, city):
        ZiruSpider().start(url, target=city + '.txt')


if __name__ == '__main__':
    spider = ZiruAllSpider()
    spider.start('http://www.ziroom.com/z/nl/z3.html')
