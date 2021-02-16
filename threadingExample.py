import threading 
import time
from random import random
  
def randomNumbers(n): 
    for nn in range(n):
        print(random())
        time.sleep(0.3)
  
def countToN(n): 
    for nn in range(n):
        print (nn)
        time.sleep(1)
        nn+=1


  
# creating thread 
t1 = threading.Thread(target=randomNumbers, args=(50,)) 
t2 = threading.Thread(target=countToN, args=(50,)) 

# starting thread 1 
t1.start() 
# starting thread 2 
t2.start() 

# wait until thread 1 is completely executed 
t1.join() 
# wait until thread 2 is completely executed 
t2.join() 

# both threads completely executed 
print("Done!") 