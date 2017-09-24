import time
from multiprocessing import Pool

def square(num):
	sum=0
	for i in range(1000):
		sum+=i*i
	return sum

if __name__=='__main__':
	t1=time.time()
	p=Pool()
	result=p.map(square,range(10000))                   #it will devide the length of core function program into different core ->see fig
	p.close()
	p.join()
	print("pool time ",time.time()-t1)
	t=time.time()
	res=[]
	for i in range(10000):
		res.append(square(i))              #sequential time will be increased as per range increases
	print("seq time ",time.time()-t)
