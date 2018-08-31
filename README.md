# ziru
自如房源数据提取
# 程序入口
1. 单个城市  
./ziru_spider.py  
2. 所有城市  
./more/ziru_all_spider.py
# 数据存储位置
1. 原始数据(json字符串)    
./data/  
2. 图片显示数据   
./pic/
# 注意
##### pyplot中文乱码问题   
1. 导入字体文件  
* 根据import matplotlib.pyplot找到matplotlib文件夹  
* 进入./mpl-data/fonts/ttf目录,放入可以识别中文的字体,如SimSun.ttf  
2. 代码申明  
plt.rcParams['font.sans-serif'] = ['SimSun'] # SimSun是你导入的字体  
plt.rcParams['axes.unicode_minus'] = False 
```
import matplotlib
from matplotlib import font_manager

# matplotlib的配置文件路径
print(matplotlib.matplotlib_fname())
# 查看支持的字体
print(sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist]))
``` 
3. 删除~/.cache/matplotlib目录下的文件  

