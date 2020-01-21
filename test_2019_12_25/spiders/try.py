start_url='http://www.cninfo.com.cn/new/index'
target=["/getAnnouces?type=sz","/getAnnouces?type=sh"]

sz_url=str(start_url+target[1])
sh_url=str(start_url+target[0])
print(sz_url)
print(sh_url)