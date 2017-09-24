import time
import threading
def square(num):
	print("cal sq num")
	for i in num:
		time.sleep(0.2)             #C.P.U will be no more in idle state
		print("sq =",i*i)


def cube(num):
	print("cal cube num")
	for i in num:
		time.sleep(0.2)          #C.P.U will be no more in idle state
		print("cu =",i*i*i)

arr=[1,2,3,4]
t=time.time() #calculate starting time to execute function
t1=threading.Thread(target=square,args=(arr,))   #create 1st thread to calculate square
t2=threading.Thread(target=cube,args=(arr,))     #create 2nd thread to calculate cube
t1.start()                     #start 1st thread
t2.start()					   #start 2nd thread
t1.join()                        #join 1st thread after completion
t2.join()						 #join 2nd thread after completion
print("time ",time.time()-t)
