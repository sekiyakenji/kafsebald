import os
import shutil
import traceback

# reading csv file and copy file and dir
# list must be 
# 1.File or Dir (F/D)
# 2.File or Dir from copy 
# 3.Dir  to copy 
try:
    index=0
    path = 'C:/tmp/list.txt'
    with open(path) as f:
        l = [s_line.strip() for s_line in f.readlines()]
        for li in l:
            y1 = li.split(',')
            print(y1[0])
            print(y1[1])
            if  y1[0] == 'F' or y1[0] == 'f':
                shutil.copy  (y1[1] , y1[2])
            else:
                if os.path.exists(y1[2]):
                    shutil.rmtree(y1[2])
                shutil.copytree (y1[1] , y1[2])
                
except: 
    print((traceback.print_exc()))