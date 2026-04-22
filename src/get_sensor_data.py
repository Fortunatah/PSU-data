## This will be to create and collect my sensor data

##  IMPORTS ##

import subprocess
import wmi

## VARIABLES ##
c = wmi.WMI(namespace="root\\wmi")
ipmi = c.Microsoft_IPMI()[0]

## functions ##

def convert_to_volts( rawData , multiplier , k2 ):
    ## take the multiplier and the k2 factors and convert them to volts
    return ( multiplier * rawData) * (10 ** k2)


def run_IPMI( address ):
    result = ipmi.RequestResponse(
        NetworkFunction=0x04,
        Lun=0x00,
        ResponderAddress=0x20,
        Command=0x2D,
        RequestDataSize=1,
        RequestData=[address]
    )

    comp_code = result[0]
    resp_data = result[1]
    if comp_code == 0: return resp_data
    else: return False

## main class ##

class IPMI_sensors():
    def __init__(self):
        self.refresh()
    def refresh(self):
        ## Go through each sensor and run it
        # 3V3
        IPMI_result = run_IPMI(0x01)
        if not IPMI_result: self.vol3v3 = "!ERROR!"
        else: 
            self.vol3v3 = convert_to_volts(IPMI_result[1] , 17 , -3 )
        # 5V
        IPMI_result = run_IPMI(0x02)
        if not IPMI_result: self.vol5v = "!ERROR!"
        else: self.vol5v = IPMI_result[1]
        # 12V
        IPMI_result = run_IPMI(0x03)
        if not IPMI_result: self.vol12v = "!ERROR!"
        else: self.vol12v = IPMI_result[1]
        # Temp
        IPMI_result = run_IPMI(0x20)
        if not IPMI_result: self.temp = "!ERROR!"
        else: self.temp = IPMI_result[1]
        # PSU1
        IPMI_result = run_IPMI(0x80)
        if not IPMI_result: self.psu1 = "!ERROR!"
        else: self.psu1 = IPMI_result[1]
        # PSU2
        IPMI_result = run_IPMI(0x81)
        if not IPMI_result: self.psu2 = "!ERROR!"
        else: self.psu2 = IPMI_result[1]

        