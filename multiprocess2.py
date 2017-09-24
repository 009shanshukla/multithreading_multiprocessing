import time
import multiprocessing
result=[]                 #declare a result obj globally
def square(num):
	global result
	for i in num:
		print("sq ",i*i)
		result.append(i*i)
	print("inside print square "+str(result))           #it will print the entire result


arr=[1,2,3,4]
t1=multiprocessing.Process(target=square,args=(arr,))             #create a thread
t1.start()					
t1.join()
print("outside print square "+str(result))		#it is empty because it will come under different process ,hence it will has a copy of result obj
print("finish")
