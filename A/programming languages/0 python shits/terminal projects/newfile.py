import sys
import time

def delete():
    sys.stdout.write('\x1b[2K')
    sys.stdout.write('\x1b[1A')
    
    

if __name__=='__main__':
    print("hello")    
    print("hello")
    delete()
    
