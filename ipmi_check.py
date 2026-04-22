import wmi

# Connect to the WMI namespace
c = wmi.WMI(namespace="root\\wmi")

# Find the IPMI instance
ipmi = c.Microsoft_IPMI()[0]

# Call RequestResponse
# Order: NetworkFunction, Lun, ResponderAddress, Command, RequestDataSize, RequestData
result = ipmi.RequestResponse(
    NetworkFunction=0x04,
    Lun=0x00,
    ResponderAddress=0x20,
    Command=0x2D,
    RequestDataSize=1,
    RequestData=[0x03]  # Note: The library handles the byte array conversion
)

# result[0] is CompletionCode (0 = Success)
# result[1] is ResponseData (The array of bytes)

if result[0] == 0:
    # Get the second byte of the response data
    raw_reading = result[1][1]
    print(f"Raw Byte Reading: {raw_reading}")
else:
    print(f"IPMI Error. Completion Code: {result[0]}")