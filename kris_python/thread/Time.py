import time


print("current time",time.localtime(time.time()))
print("current format time",time.asctime(time.localtime(time.time())))
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
a = "Sat Mar 28 22:24:24 2016"
# print(time.mktime(time.strftime(a,"%a %b %d %H:%M:%S %Y")))
