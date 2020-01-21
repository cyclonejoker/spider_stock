import time,datetime
timestamp=1577980800      ##不像是时间戳
#转化成localtime
# t=timestamp.replace('','')[:-1]
time_local=time.localtime(timestamp)
dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
print(dt)