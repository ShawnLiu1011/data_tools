import os
import shutil

def dataset(pathdir):
	trainlist = []
	testlist = []
	for cls in os.listdir(pathdir):
		fTrain = open(pathdir+cls+'/trainval.txt')
		fTest = open(pathdir+cls+'/test.txt')
		line = fTrain.readline()
		row = 0
		while(line and row<20):
			trainlist.append(line)
			line = fTrain.readline()
			row+=1
		row = 0
		line = fTest.readline()
		while(line and row<10):
			testlist.append(line)
			line = fTest.readline()
			row+=1
	trainlist = list(set(trainlist))
	testlist = list(set(testlist))
	trainlist.sort()
	testlist.sort()
	fTrain = open('trainval.txt','w')
	for t in trainlist:
		fTrain.write(t)
	fTest = open('test.txt','w')
	for t in testlist:
		fTest.write(t)
	fTrain.close()
	fTest.close()

	#with open('data.txt','w') as f:    #设置文件对象
	#	f.write(Counter(category)) 
	#	f.write(total_num) 
 
if __name__ == '__main__':
	# pathdirs = list(set(os.listdir('./')) ^ set(['tools','count.py']))
	# print(pathdirs)
	# for pathdir in pathdirs:
	pathdir = 'F:/无人超市/transformer/'
	dataset(pathdir)
