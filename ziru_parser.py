from bs4 import BeautifulSoup

'''
解析从网络中获取到的数据
'''


class ZiruParser:

    def __init__(self):
        self.main_url = ''

    def set_main_url(self, main_url):
        self.main_url = main_url

    # 传入一个url和此url返回的数据
    def parse(self, page_url, content):
        if page_url is None or content is None:
            return None, None
        soup = BeautifulSoup(content, 'lxml', from_encoding='utf-8')
        # print(soup.prettify())
        new_urls = self._get_new_urls(page_url, soup)
        new_date = self._get_new_date(page_url, soup)
        return new_urls, new_date

    # 解析新的url
    def _get_new_urls(self, page_url, soup):
        source = soup.find('div', class_='pages', id='page')
        new_urls = set()
        link_node = source.find('a', class_='next')
        if link_node:
            new_url = self.main_url + link_node.get('href').replace('//', '')
            new_urls.add(new_url)
        return new_urls

    # 解析数据
    def _get_new_date(self, page_url, soup):

        sources = soup.find_all(name='div', class_='txt')
        urls = []
        locations = []
        detals = []
        for source in sources:
            # 地理位置
            address = source.find_all(name='a', target='_blank')
            location = [address[0].get_text(), address[1].get_text()]
            # 链接地址
            url = address[0]['href'].replace('//', '')
            urls.append(url)
            locations.append(location)
            # 房源详情
            detal = source.find(name='div', class_='detail')
            d = detal.get_text().replace(' ', '').replace('\n', '')
            detals.append(d)

        # 将获取的信息封装到一个数组
        infos = []
        for i in range(len(urls)):
            infos.append({'url': urls[i], 'location': locations[i], 'detal': detals[i]})
        # print(infos)
        return infos
