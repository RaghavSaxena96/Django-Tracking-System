from django.http import HttpResponse
from matplotlib import pylab
from pylab import *
import PIL, PIL.Image, StringIO
import matplotlib 
import matplotlib.pyplot as plt
import time
import random
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

#ysample = random.sample(xrange(-50, 50), 100)
 
xdata = []
ydata = []
 
plt.ion()
fig = plt.figure()
axes = fig.add_subplot(111)
plt.show()

'''
axes = plt.gca()'''
axes.set_xlim(0, 200)
axes.set_ylim(0,200)
line, = axes.plot(xdata, ydata, 'r-')
p=10;
print(type(p))
i=0
while(1):
	r.set_response_callback('HGET', float)
	x = r.hget("forklift1","x")
	y = r.hget("forklift1","y")
	xdata.append(x*10)
	ydata.append(y*10)
	print(xdata)
	line.set_xdata(xdata)
	line.set_ydata(ydata)
	fig.canvas.draw();
	plt.pause(1e-17)
	time.sleep(0.1)
	if(i>=20):
		del xdata[0]
		del ydata[0]
	i=i+1
	


# add this if you don't want the window to disappear at the end
#plt.show()
