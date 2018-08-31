import matplotlib
from matplotlib import font_manager

# matplotlib的配置文件路径
print(matplotlib.matplotlib_fname())
# 查看支持的字体
print(sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist]))


from util.downloader import DownLoader
from ziru_parser import ZiruParser
from ziru_saver import ZiruSaver

url = 'http://www.ziroom.com/z/nl/z3.html?p=50'
downloader = DownLoader()
content = downloader.download(url)
# print(content)

parser = ZiruParser()
new_urls, new_date = parser.parse(url, content)
print(new_date)
print(new_urls)
if new_urls:
    print('====')

saver = ZiruSaver()
saver.collect_data(new_date)
saver.save_data()
