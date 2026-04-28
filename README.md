"# AMAT PSU Data Monitor

A Python-based GUI application for monitoring power supply unit (PSU) voltages, temperatures, and status on Applied Materials systems using IPMI (Intelligent Platform Management Interface) sensors.

## Overview

This application provides real-time monitoring of critical power and thermal parameters through an intuitive tkinter-based graphical interface. It communicates with the system's IPMI interface to collect sensor data and displays it in a compact, color-coded display window.

## Features

- **Real-time Voltage Monitoring**
  - 5V rail voltage
  - 3.3V rail voltage
  - 12V rail voltage

- **Thermal Monitoring**
  - CPU/system temperature in °C

- **Power Supply Status**
  - PSU1 status monitoring
  - PSU2 status monitoring
  - Detects AC failures and PSU removal

- **Color-Coded Display**
  - Green: All systems operational ("OK")
  - Red: Error states, PSU removed, or AC power lost
  - Black: Normal voltage readings

- **Automatic Data Refresh**
  - Updates sensor data every 1000ms (1 second)
  - Continuously monitors system state

## Project Structure

```
PSU-data/
├── main.py                 # Entry point - launches the main application
├── README.md              # This file
├── pictures/
│   └── applied_materials.ico  # Application icon
└── src/
    ├── __init__.py        # Package initialization
    ├── app.py            # Main GUI application (tkinter)
    └── get_sensor_data.py # IPMI sensor data collection
```

## Requirements

### System Requirements
- Windows OS with IPMI support
- Applied Materials system with IPMI interface
- Python 3.6+

### Python Dependencies
- `tkinter` - GUI framework (included with Python)
- `wmi` - Windows Management Instrumentation
- `pypiwin32` - WMI interface support (required for wmi module)

### Installation

1. Install required Python packages:
```bash
pip install wmi pypiwin32
```

2. Run the post-install script for pypiwin32:
```bash
python Scripts/pywin32_postinstall.py -install
```

## Usage

Run the application from the command line:

```bash
python main.py
```

Or directly from the src directory:

```python
import src
src.app_main()
```

## Technical Details

### IPMI Sensor Addresses

The application queries the following IPMI sensor addresses:

| Sensor | Address | Measurement | Unit |
|--------|---------|-------------|------|
| 3.3V Rail | 0x01 | Voltage | V |
| 5V Rail | 0x02 | Voltage | V |
| 12V Rail | 0x03 | Voltage | V |
| Temperature | 0x20 | Temperature | °C |
| PSU1 Status | 0x80 | Status | - |
| PSU1 Voltage | 0x7A | Voltage | V |
| PSU2 Status | 0x81 | Status | - |
| PSU2 Voltage | 0x7B | Voltage | V |

### Data Conversion

Voltage readings are converted from raw IPMI data using:
```
Voltage = (Multiplier × RawData) × 10^K2
```

Where multipliers and K2 factors are specific to each sensor.

### Error States

- **!ERROR!** - IPMI communication failure
- **!NO IPMI!** - IPMI interface not available/detected
- **!PSU REMOVED!** - Power supply unit not present
- **!AC REMOVED!** - AC power input lost

## GUI Layout

The application displays a compact window (200x180 pixels) with the following fields:

```
5V        [Value]
3.3V      [Value]
12V       [Value]
Temp      [Value]
PSU1      [Value]
PSU2      [Value]
```

Values update automatically every second.

## Architecture

### main.py
Entry point that imports and executes `app_main()` from the src package.

### src/app.py
Contains the tkinter GUI implementation:
- `configure_window()` - Creates GUI labels and entry boxes
- `data_to_entry()` - Updates display boxes with color coding
- `check_for_ipmi()` - Verifies IPMI interface availability
- `app_main()` - Main application loop with auto-refresh logic

### src/get_sensor_data.py
Handles IPMI communication:
- `IPMI_sensors` class - Manages sensor data collection
- `run_IPMI()` - Executes IPMI commands
- `convert_to_volts()` - Converts raw sensor data to voltage readings

## Troubleshooting

### "!NO IPMI!" appears in all fields
- IPMI interface is not available or not accessible
- Check that the system supports IPMI
- Verify user has appropriate permissions for IPMI access
- Ensure WMI configuration is correct

### Values show "!ERROR!"
- IPMI communication failure
- Check system stability and IPMI service status
- Verify all power supplies are connected

### Application won't start
- Ensure Python 3.6+ is installed
- Verify all dependencies are installed: `pip install wmi pypiwin32`
- Check that you're running on Windows
- Run post-install script for pypiwin32

## License

Applied Materials - Internal Use

## Notes

- Application requires Windows operating system
- IPMI must be enabled and accessible on the target system
- Application runs indefinitely and updates every second until closed
- Window is resizable but optimal size is 200x180 pixels" 
