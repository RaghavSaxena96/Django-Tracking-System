import math
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import redis
import json


r = redis.Redis(host='localhost', port=6379, db=0)



x=5
y=6

for i in range(0,100):
    data={}
    data['x']=x+1
    data['y']=y+2
    x=x+1
    y=y+1
    data['forklift']="forkilft1"
    li=[]
    li.append(data);
    json_data=json.dumps(li)
    r.hset(data['forklift'],'x',data['x'],'y',data['y'])
    print(json_data)


