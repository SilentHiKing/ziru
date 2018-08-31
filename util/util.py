# coding=utf-8

from bs4 import BeautifulSoup
import requests
import random
import re
import time
import os


# 打印方法执行时间
def run_time(func):
    def wrapper(self, *args, **kw):
        start = int(round(time.time() * 1000))
        print('start_time:%s' % str(start))
        result = func(self, *args, **kw)
        end = int(round(time.time() * 1000))
        print('end_time:%s' % str(end))
        print('call method:%s  time=%sms' % (func.__name__, str(end - start)))
        return result

    return wrapper


# IP地址取自国内髙匿代理IP网站：http://www.xicidaili.com/nn/
# 仅仅爬取首页IP地址就足够一般使用
class Util(object):
    url = 'http://www.xicidaili.com/nn/'
    proxies = {}

    # 获取代理ip
    def get_proxies(self, url=url, headers=None):
        return None
        if Util.proxies:
            return Util.proxies
        headers = (headers if headers else self.get_headers())
        print('headers%s' % headers)
        web_data = requests.get(url, headers=headers)
        soup = BeautifulSoup(web_data.text, 'lxml')
        ips = soup.find_all('tr', class_=['', 'odd'])
        ip_list = []
        try:
            for i in range(len(ips)):
                ip_info = ips[i]
                tds = ip_info.find_all('td')
                ip_list.append(tds[1].text + ':' + tds[2].text)
                # print tds[one].text + ':' + tds[2].text
        except Exception as e:
            print(e.message)
        # print ip_list
        if ip_list:
            return self.get_random_ip(ip_list)
        else:
            return None

    def get_random_ip(self, ip_list):
        proxy_ip = random.choice(ip_list)
        proxy_ip = 'http://' + proxy_ip
        Util.proxies['http'] = proxy_ip
        print(Util.proxies)
        return Util.proxies

    # 读取cookie数据
    def get_cookies(self):
        abs_path = os.path.dirname(__file__)  # 绝对路径
        path = os.path.join(abs_path, 'cookie.txt')
        print("abs path is %s" % abs_path)
        try:
            with open(path, 'r') as f:
                cookies = {}
                for line in f.read().split(';'):
                    name, value = line.strip().split('=', 1)
                    cookies[name] = value
                return cookies
        except Exception as e:
            return None

    def get_headers(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'
        }
        return headers
