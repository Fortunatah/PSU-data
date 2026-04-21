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

def parse_lines(line , target):
    split_line = line.split()
    for index, word in enumerate(split_line):
        if word == target: return split_line[index - 1]
    ## if it does not see volts
    return "FAIL"


def run_IPMI():
    IPMI_path = "ipmiutil\\ipmiutil.exe"
    result  = subprocess.run([ IPMI_path , "sensor"] 
                             , capture_output=True, text = True)
    
    ## Grab raw output and only grab what we need
    raw_output = result.stdout
    needed_lines = []
    for line in raw_output.split("\n"):
        if line[:4] in needed_vals:
            needed_lines.append(line)
    return needed_lines

## main class ##

class IPMI_sensors():
    def __init__(self):
        self.refresh()
    def refresh(self):
        ## refresh the results and parse the data
        result = run_IPMI()
        for line in result:
            ## go through list and define needed values
            if line[:4] == needed_vals[0]:
                self.vol3v3 = parse_lines(line , "Volts")
            if line[:4] == needed_vals[1]:
                self.vol5v = parse_lines(line , "Volts")
            if line[:4] == needed_vals[2]:
                self.vol12v = parse_lines(line , "Volts")
            if line[:4] == needed_vals[3]:
                self.temp = parse_lines(line , "degrees")

        