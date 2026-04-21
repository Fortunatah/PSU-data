## This will be to create and collect my sensor data

##  IMPORTS ##

import subprocess

## functions ##

def run_IPMI():
    IPMI_path = "ipmiutil\\ipmiutil.exe"
    result  = subprocess.run([ IPMI_path , "sensor"] 
                             , capture_output=True, text = True)
    return result

## main class ##

class IPMI_sensors():
    def __init__(self):
        result = run_IPMI()
        for line in result:
            print(f"line = {line}")