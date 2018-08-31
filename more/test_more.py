from downloader import DownLoader
from five.ziru_parser import ZiruParser
from five.ziru_saver import ZiruSaver

url = 'http://www.ziroom.com/z/nl/z3.html?p=50'
downloader = DownLoader()
content = downloader.download(url)
# print(content)