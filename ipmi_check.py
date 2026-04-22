import wmi

# Connect to the WMI namespace
c = wmi.WMI(namespace="root\\wmi")
ipmi = c.Microsoft_IPMI()[0]

# Mapping the sensor IDs from your ipmiutil output
# Mapping the sensor IDs
sensors = {
    "3.3V (P_3V3)": 0x01,
    "5V (P_5V)":    0x02,
    "12V (P_12V)":  0x03,
    "SYS1_Temp":    0x20,
    "PSU1_Status":    0x80, # Discrete sensor
    "PSU2_Status":    0x81  # Discrete sensor
}

print("--- IPMI Sensor Readings ---")

for name, snum in sensors.items():
    # Call the WMI method
    # Returns a tuple: (CompletionCode, ResponseData, ResponseDataSize)
    result = ipmi.RequestResponse(
        NetworkFunction=0x04,
        Lun=0x00,
        ResponderAddress=0x20,
        Command=0x2D,
        RequestDataSize=1,
        RequestData=[snum]
    )

    comp_code = result[0]
    resp_data = result[1]

    if comp_code == 0:
        # resp_data[1] is the actual raw reading byte
        print(f"{name:15} | Raw Hex: {hex(resp_data[1])} | Decimal: {resp_data[1]}")
    else:
        print(f"{name:15} | Failed with Completion Code: {comp_code}")