import os
import shutil
import traceback
#f = open(r'C:\Users\UserName\Desktop\test.json','r',encoding="utf-8")

try:
    FROMDIR = 'C:/tmp/aa/'
    TODIR   = 'C:/tmp/bb/'
    
    files = os.listdir(FROMDIR)
    for f in files:
        shutil.copy  (FROMDIR +  f, TODIR  + f)

    str = 'abc_de'    
    l = list(str)
    print(str[0:l.index('_')])

except:
    print((traceback.print_exc()))

