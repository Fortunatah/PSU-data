## This will be to create and collect my sensor data

##  IMPORTS ##

import subprocess
import os

## FUNCTIONS ##

def gsd_main():
    IPMI_path = "ipmiutil\\ipmiutil.exe"
    result  = subprocess.run([ IPMI_path , "sensor"] 
                             , capture_output=True, text = True)
    
    print(result.stdout)