
# coding:utf-8
import xml.etree.cElementTree as ET
import os
from collections import Counter
import shutil
 
# Counter({'towCounter({'tower': 3074, 'windpower': 2014, 'thermalpower': 689, 'hydropower': 261, 'transformer': 225})
# total_num: 6263
 
def divide_class(pathdir,despath):
	category = []
	path = pathdir + 'Annotations/'
	for index,xml in enumerate(os.listdir(path)):
		# print(str(index) + ' xml: '+ xml)
		root = ET.parse(os.path.join(path, xml))
		objects = root.findall('object')
		
		# ==================select images which has a special object=============
		
		for obj in objects:
			obj_label = obj.find('name').text.strip()

			imgfile = pathdir + 'JPEGImages/' + xml.replace('xml', 'jpg')
			img_despath = despath + obj_label
			if not os.path.exists(img_despath):
				os.makedirs(img_despath)
			shutil.copy(imgfile, img_despath)
 		
		# ==================select images which has a special object=============
 
		category += [ob.find('name').text for ob in objects]
	print(Counter(category))
	total_num = sum([value for key, value in Counter(category).items()])
	print('total_num:',total_num)

	#with open('data.txt','w') as f:    #设置文件对象
	#	f.write(Counter(category)) 
	#	f.write(total_num) 
 
if __name__ == '__main__':
	# pathdirs = list(set(os.listdir('./')) ^ set(['tools','count.py']))
	# print(pathdirs)
	# for pathdir in pathdirs:
	pathdir = 'F:/无人超市/market/'
	despath = 'F:/无人超市/transformer/'
	divide_class(pathdir,despath)
