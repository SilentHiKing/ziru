import re

from bs4 import BeautifulSoup

'''
解析从网络中获取到的数据
'''


class ZiruAllParser:

    def __init__(self):
        self.main_url = 'http:'

    def set_main_url(self, main_url):
        self.main_url = main_url

    # 传入一个url和此url返回的数据
    def parse(self, page_url, content):
        if page_url is None or content is None:
            return None, None
        soup = BeautifulSoup(content, 'lxml', from_encoding='utf-8')
        # print(soup.prettify())
        new_date = self._get_new_date(page_url, soup)
        return new_date

    # 解析数据
    def _get_new_date(self, page_url, soup):
        sources = soup.find(name='dl', class_='changeCityList')
        # ['网址','城市'] 作为元素存储到数组
        infos = []
        source = sources.find_all(name='a', class_=re.compile('.*bor*'))
        for s in source:
            url = self.main_url + s.get('href')
            city = s.get_text()
            infos.append([url, city])
        return infos
