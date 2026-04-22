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

# result[0] is the ResponseData (the bytes we saw earlier)
# result[0][1] is your raw hex reading
print(f"Raw Byte Reading: {result[0][1]}")