#!/usr/bin/env python
import os
import sys
import threading
import names
import time

def hello(file_name, count):
    with open(file_name, 'a', 1) as f:
        for i in range(0, count):
            f.write(names.get_full_name() + os.linesep)

if __name__ == '__main__':    
    #start a file
    start = int(time.time())
    with open('some.txt', 'w') as f:
        f.write('this is the beginning' + os.linesep)
    #make 10 threads write a million lines to the same file at the same time
    threads = []
    for i in range(0, 10):
        threads.append(threading.Thread(target=hello, args=('some.txt', 10000)))
        threads[-1].start()
    for t in threads:
        t.join()
        #check what the heck the file had
        uniq_lines = set()
    with open('some.txt', 'r') as f:
        for l in f:
            uniq_lines.add(l)
    for u in uniq_lines:
        sys.stdout.write(u)
    stop = int(time.time())
    print('Time taken',stop-start)
