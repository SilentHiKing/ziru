from downloader import DownLoader
from five.ziru_parser import ZiruParser
from five.ziru_saver import ZiruSaver

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
