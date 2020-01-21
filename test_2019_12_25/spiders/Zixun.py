# -*- coding: utf-8 -*-
import scrapy
from ..items import Zixun_decreaseItem,Zixun_shItem,Zixun_szItem
import json
import datetime
import logging
from scrapy.mail import MailSender
class ZixunSpider(scrapy.Spider):
    name = 'Zixun'
    allowed_domains = ['http://www.cninfo.com.cn/new/index']


    def start_requests(self):
        query_base_url='http://www.cninfo.com.cn/new/hisAnnouncement/query'
        now=str(datetime.datetime.now().strftime('%Y-%m-%d'))
        query_date=now+'~'+now
        requests=[]
        for pageNum in range(1,4):
            data={
                'pageNum':str(pageNum),
                'pageSize':'30',
                'column':'szse',
                'tabName':'fulltext',
                'plate':'sz;sh',
                'stock':'',
                'searchkey':'减持;质押;实际控制人',
                'secid':'',
                'category':'',
                'trade':'',
                'seDate':query_date,
                'sortName':'',
                'sortType':'',
                'isHLtitle':'',
            }
            request=scrapy.FormRequest(url=query_base_url,callback=self.decrease_operate,formdata=data)
            requests.append(request)
        investigate_data={
            'searchkey':'投资者调研',
            'seDate':query_date,
            'isfulltext':'false',
            'sortName':'',
            'sortType':'',
            'pageNum':'1'
        }
        investigate_request=scrapy.FormRequest(url=query_base_url,callback=self.investigate_operate,formdata=investigate_data)
        requests.append(investigate_request)
        return requests
        # requests=[]
        # sh_url=str(start_url+target[0])
        # sh_request=scrapy.Request(url=sh_url,method='get',callback=self.sh_operate,encoding='utf-8')
        # requests.append(sh_request)
        # sz_url=str(start_url+target[1])
        # sz_request=scrapy.Request(url=sz_url,method='get',callback=self.sz_operate,encoding='utf-8')
        # requests.append(sz_request)
        # for i in range(1,3):
        #     query_url=str(query_base_url+str(i))
        #     request=scrapy.Request(url=query_url,method='get',callback=self.decrease_operate,encoding='utf-8')
        #     requests.append(request)
        # return requests
    def sh_operate(self,response):
        print("正在爬取上交数据")
        JsonBody=json.loads(response.body)
        data=JsonBody["classifiedAnnouncements"]
        for Father_target in data:
            for target in Father_target:
                item=Zixun_shItem()
                item["secCode"]=target["secCode"]
                item["secName"]=target["secName"]
                item["announcementTitle"]=target["announcementTitle"]
                item["announcementTime"]=target["announcementTime"]
                item["file_urls"]="http://static.cninfo.com.cn/"+target["adjunctUrl"]
                item['zixun_type']='sh'
                yield item
    def sz_operate(self,response):
        print("正在爬取深交数据")
        JsonBody=json.loads(response.body)
        data=JsonBody["classifiedAnnouncements"]
        for Father_target in data:
            for target in Father_target:
                item=Zixun_szItem()
                item["secCode"]=target["secCode"]
                item["secName"]=target["secName"]
                item["announcementTitle"]=target["announcementTitle"]
                item["announcementTime"]=target["announcementTime"]
                item["file_urls"]="http://static.cninfo.com.cn/"+target["adjunctUrl"]
                item['zixun_type']='sz'
                yield item
    def decrease_operate(self,response):
        print("正在爬取减持数据")
        JsonBody=json.loads(response.body)
        data=JsonBody["announcements"]
        for target in data:
            item=Zixun_decreaseItem()
            item["secCode"]=target["secCode"]
            item["secName"]=target["secName"]
            announcementTitle=str(target["announcementTitle"]).replace("</em>",'').replace("<em>",'')
            item["announcementTitle"]=announcementTitle
            item["announcementTime"]=target["announcementTime"]
            item["file_urls"]="http://static.cninfo.com.cn/"+target["adjunctUrl"]
            item["zixun_type"]='decrease'
            yield item
    def investigate_operate(self,response):
        print("正在爬取投资者数据")
        JsonBody=json.loads(response.body)
        data=JsonBody["announcements"]
        for target in data:
            item=Zixun_decreaseItem()
            item["secCode"]=target["secCode"]
            item["secName"]=target["secName"]
            announcementTitle=str(target["announcementTitle"]).replace("</em>",'').replace("<em>",'')
            item["announcementTitle"]=announcementTitle
            item["announcementTime"]=target["announcementTime"]
            item["file_urls"]="http://static.cninfo.com.cn/"+target["adjunctUrl"]
            item["zixun_type"]='investigate'
            yield item