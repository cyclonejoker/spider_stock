import time 
import os
while True:
    # os.system("conda activate spider_env")
    os.system("cd .\\news\\")
    os.system("scrapy crawl Zixun")
    time.sleep(86400) #每隔一天运行一次 24*60*60=86400s