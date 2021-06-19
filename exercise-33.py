#exercise33
#digital time with "Time modules"
from time import *
while True:
    seconds = time()
    print("\r",ctime(seconds),end = " ")
    sleep(1)