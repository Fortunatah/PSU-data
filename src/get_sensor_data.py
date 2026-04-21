## This will be to create and collect my sensor data

##  IMPORTS ##

import subprocess

## VARIABLES ##
needed_vals = [
    "0001", ## 3V3
    "0002", ## 5V
    "0003", ## 12V
    "0017"  ## Sys 1 temp
]

## functions ##

def run_IPMI():
    IPMI_path = "ipmiutil\\ipmiutil.exe"
    result  = subprocess.run([ IPMI_path , "sensor"] 
                             , capture_output=True, text = True)
    raw_output = result.stdout

    for line in raw_output.split("\n"):
        print(line[:3])

## main class ##

class IPMI_sensors():
    def __init__(self):
        result = run_IPMI()
        