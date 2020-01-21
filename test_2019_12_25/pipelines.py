# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import sys
import datetime
import csv
import time
import scrapy
from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import DropItem
from urllib.parse import urlparse
# from testpdfReader import pdfToText
from test_2019_12_25.pdfReader import pdfToText

# from util.pdfReader import pdfToText
# from test_2019_12_25.pdfReader import pdfToText

class Test20191225Pipeline(object):
    def process_item(self, item, spider):
        return item
class Tradeline(object):
    def make_csv(self,info_type):
        csv_name=str(datetime.datetime.now().strftime('%Y-%m-%d'))+str(info_type)+".csv"
        # store_file=os.path.dirname(__file__)+'\save\\'+str(csv_name)
        store_file='E:\Intership\spider_test\json\\'+csv_name
        self.file=open(store_file,'a')
        self.writer=csv.writer(self.file)
        
    def process_item(self,item,spdier):
        # if item.get()
        ##要转化成utf8 否则 会写不进去
        str.encode('utf-8')
        if item['secCode']:
            
            ##  新建对应csv
            self.make_csv(item['zixun_type'])
            ##时间转化
            timestamp=int(item['announcementTime'])/1000
            time_local=time.localtime(timestamp)
            dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
            # print(os.path.basename(item['file_urls']))
            path='E:\Intership\spider_test\pdf\\'+os.path.basename(item['file_urls'])
            content=pdfToText(path).replace('\n','')
            key_word="证券"
            if key_word in content:
                self.writer.writerow((str(item['secCode']),str(item['secName']),str(item['announcementTitle']),str(dt),content))
            else:
                self.writer.writerow((str(item['secCode']),str(item['secName']),str(item['announcementTitle']),str(dt)))

            # print(content)
            ## pdf 转化
            # file_path="E:\Intership\spider_test\pdf\\"+str(item['files'][0]['path'])
            # content=pdfToText(file_path)            
            # Files 内部数据类型[{'url': 'http://static.cninfo.com.cn/finalpage/2020-01-03/1207219806.PDF', 'path': '1207219806.PDF', 'checksum': '63d052e4155c20c7550634d31682cadd'}]
            # self.writer.writerow((str(item['secCode']),str(item['secName']),str(item['announcementTitle']),str(dt)))
            # self.writer.writerow((item['secCode'].encode('utf8','ignore'),item['secName'].encode('utf8','ignore'),item['announcementTitle'].encode('utf8','ignore'),item['announcementTime'],item['adjunctUrl'].encode('utf8','ignore')))
        return item

# class FilePipeline(FilesPipeline):
#     def file_path(self,request,response=None,info=None):
class MyFilesPipeline(FilesPipeline):

    def get_media_requests(self, item, info):
        file_url = item['file_urls']
        meta = {'filename': item['secName']}
        # print('%s',item['files']['path'])
        # print('%s',item['files']['path'])
        # print(item['announcementTitle'])
        self.announcementTitle=item['announcementTitle']
        # yield sRequest(url=file_url, meta=meta)
        yield scrapy.Request(url=file_url,meta=meta)
        
    def file_path(self, request, response=None, info=None):
        parse_result = urlparse(request.url)
        # print('parse_result:',parse_result)
        path = parse_result.path
        # print(path)
        basename2 = os.path.basename(path)
        ###测试了一下 发现好像因为文件名字太长或者有特殊字节，修改成中文的时候。 下载不能
        basename=self.announcementTitle+'.PDF'
        # print(basename)
        # print(basename2)
        # print(basename)
        # print('basename',basename)
        return basename2 