import multiprocessing
import time
def deposit(bal,lock):
	for i in range(200):
		time.sleep(0.01)
		lock.acquire()    #lock is acquired because if it will not be there then in some cases in assemble language before assignment to final value it will jump to next process
		bal.value=bal.value+1
		lock.release()

def withdraw(bal,lock):
	for i in range(200):
		time.sleep(0.01)
		lock.acquire()
		bal.value=bal.value-1
		lock.release()


if __name__=='__main__':
	bal=multiprocessing.Value('i',200)
	lock=multiprocessing.Lock()                        #here we get a lock 
	d=multiprocessing.Process(target=deposit,args=(bal,lock))
	w=multiprocessing.Process(target=withdraw,args=(bal,lock))
	d.start()
	w.start()
	d.join()
	w.join()
	print(bal.value)
