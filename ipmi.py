import wmi


def check_for_ipmi():
    try:
        c = wmi.WMI(namespace="root\\wmi")
        ipmi_class = getattr(c, "Microsoft_IPMI", None)
        
        if ipmi_class:
            instances = ipmi_class()
            if instances:
                return instances[0] # Returns the actual connection object
        return None
    except Exception:
        return None

# Usage:
ipmi_conn = check_for_ipmi()
if ipmi_conn:
    # Do work
    data = ipmi_conn.GetSensorData(SensorNumber=1)