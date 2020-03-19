import json
import time
import threading


def sleepTest():
    time.sleep(3)
    print("thread start")

Object = {
    "name":"lamber",
    "age":1
}
json_str=json.dumps(Object)
print(Object)
print(json_str)


data = json.loads(json_str)
print(data)