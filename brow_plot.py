import matplotlib
matplotlib.use('WebAgg')
import matplotlib.pyplot as plt,mpld3
from django.http import HttpResponse
from matplotlib import pylab
from pylab import *
import PIL, PIL.Image, StringIO
import time
import random
import redis

fig1 = plt.figure()
plt.xlabel('RelativeTime (ms)')
plt.ylabel('AbsoluteTime (ms)')
plt.title('R-A Combinations')


xdata = []
ydata = []
 
plt.ion()
fig = plt.figure()
axes = fig.add_subplot(111)
plt.show()
'''
axes = plt.gca()'''
axes.set_xlim(0, 500)
axes.set_ylim(0,500)
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
	


    
print ('<HTML><HEAD><TITLE>Python Matplotlib Graph</TITLE></HEAD>')
print ('<BODY>')
print ('<CENTER>')
print ('<br><br>')
print ('<H3>Graph</H3>')
print (mpld3.fig_to_html(fig1, d3_url=None, mpld3_url=None, no_extras=False, template_type='general', figid=None, use_http=False))
print ('<br>')

print ('</CENTER>')
print ('</BODY>')
print ('</html>')
