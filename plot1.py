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

while(1):
    data={}
    data['x']=float(x+1)/100
    data['y']=float(y+2)/100
    x=x+0.001
    y=y+0.001
    print(x);
    data['forklift']="forklift1"
    li=[]
    li.append(data);
    json_data=json.dumps(data)
    #point = {"x" : data['x'], "y" : data['y']}
    r.hset(data['forklift'],"x" , data['x'] )
    r.hset(data['forklift'],"y" , data['y'] )
    #print(r.hgetall(data['forklift']))
    #print(json_data)
print(json_data);
