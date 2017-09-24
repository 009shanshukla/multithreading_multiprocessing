import time
import multiprocessing

def square(num,res,val):
	val.value=0.6
	for idx,n in enumerate(num):             #this is the method to append shared array
		res[idx]=n*n
	print("inside result square ",res[:])
	print("inside val ",val.value)



arr=[1,2,3,4]
res=multiprocessing.Array('i',4)                      #this array will be shared between mainn process and p process
val=multiprocessing.Value('d',0.0)						#this value will be shared between mainn process and p process
p=multiprocessing.Process(target=square,args=(arr,res,val))
p.start()
p.join()
print("outside result square ",res[:])              #this is the method to print shared array
print("outside val ",val.value)
