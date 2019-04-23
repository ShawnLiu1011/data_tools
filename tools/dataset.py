import os
import shutil

def dataset(pathdir):
	for cls in os.listdir(pathdir):
		fTrain =  open(pathdir+cls+'/trainval.txt','w')
		fTest = open(pathdir+cls+'/test.txt','w')
		filelist = os.listdir(pathdir+cls)
		line = int(2*len(filelist)/3)
		for file in filelist[:line]:
			fTrain.write('{}\n'.format(file[0:-4]))#去掉.txt
		for file in filelist[line:-2]:
			fTest.write('{}\n'.format(file[0:-4]))#去掉.txt


	#with open('data.txt','w') as f:    #设置文件对象
	#	f.write(Counter(category)) 
	#	f.write(total_num) 
 
if __name__ == '__main__':
	# pathdirs = list(set(os.listdir('./')) ^ set(['tools','count.py']))
	# print(pathdirs)
	# for pathdir in pathdirs:
	pathdir = 'F:/无人超市/transformer/'
	dataset(pathdir)
