import time
import multiprocessing

def square(num):
	for i in num:
		print("starting square")
		print("sq ",i*i)
		time.sleep(0.5)


def cube(num):
	for i in num:
		print("starting cube")
		print("cu ",i*i*i)
		time.sleep(0.5)	

arr=[1,2,3,4]
t1=multiprocessing.Process(target=square,args=(arr,))                #create 1st process
t2=multiprocessing.Process(target=cube,args=(arr,))					#create 2nd process
t1.start()                       #both process will have different memory segment
t2.start()
t1.join()
t2.join()
print("finish")
