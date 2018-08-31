import requests
from util.util import Util
import chardet

'''
请求网络获取数据
'''


class DownLoader(object):

    def __init__(self):

        util = Util()
        self.cookies = util.get_cookies()
        self.headers = util.get_headers()
        self.proxies = util.get_proxies()
        print(self.headers)
        print(self.cookies)

    def download(self, url):
        if url is None:
            return None
        response = requests.get(url, cookies=self.cookies, headers=self.headers, proxies=self.proxies)

        if response.status_code != 200:
            print('error code : %d in %s' % (response.status_code, url))
            print(response.content)
            return None
        # print(response.text)
        return response.content
