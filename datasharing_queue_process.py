import multiprocessing

def square(num,res):
	for i in num:
		res.put(i*i)


arr=[1,2,3,4]
res=multiprocessing.Queue()
p=multiprocessing.Process(target=square,args=(arr,res))                   #this queue is shared between main and p process
p.start()
p.join()
while res.empty() is False:
	print(res.get())
