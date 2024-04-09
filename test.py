import threading
from time import sleep
 
def proc(n):
   print("Процесс", n)
   sleep(5)

for i in range(10): 
    threading.Thread(target=proc, name="t"+str(i), args=[str(i)]).start()
