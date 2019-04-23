
# coding:utf-8
import os
from collections import Counter
import shutil
 
# Counter({'towCounter({'tower': 3074, 'windpower': 2014, 'thermalpower': 689, 'hydropower': 261, 'transformer': 225})
# total_num: 6263
 
def order_rename(pathdir,start):
	path = pathdir + 'Annotations/'
	i = start
	for index,xml in enumerate(os.listdir(path)):
		# print(str(index) + ' xml: '+ xml)
		imgfile = pathdir + 'JPEGImages/' + xml.replace('xml', 'jpg')
		os.rename(path + xml, path +'%06d' % i + '.xml')
		os.rename(imgfile, pathdir + 'JPEGImages/' + '%06d' % i + '.jpg')
		i = i + 1

	#with open('data.txt','w') as f:    #设置文件对象
	#	f.write(Counter(category)) 
	#	f.write(total_num) 
 
if __name__ == '__main__':
	# pathdirs = list(set(os.listdir('./')) ^ set(['tools','count.py']))
	# print(pathdirs)
	# for pathdir in pathdirs:
	pathdir = 'F:/无人超市/all_20190407180240/all/'
	i = 5000
	order_rename(pathdir,i)
