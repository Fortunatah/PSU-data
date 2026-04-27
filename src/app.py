## This will be where my main app lives
## We will run it from app_main

## Reference for value_boxes
"""
[
    '5V', -> value_boxes[0]
    '3.3V', -> value_boxes[1]
    '12V', -> value_boxes[2]
    'Temp', -> value_boxes[3]
    'PSU1', -> value_boxes[4] 
    'PSU2' -> value_boxes[5]
]
"""
## import modules
import tkinter as tk
import ctypes
from .get_sensor_data import IPMI_sensors

## variables

needed_values = [
    '5V',
    '3.3V',
    '12V',
    'Temp',
    'PSU1',
    'PSU2'
]

## configure entry boxes

def data_to_entry(box , value ):
    # if failure have it be red
    bad_values = ["!ERROR!" , "!PSU REMOVED!" , "!AC REMOVED!"]
    if value in bad_values:
        box.insert(0, f"{value}")
        box.config(fg="red")
    # if the power is ok print green
    elif value == "OK":
        box.insert(0, f"{value}")
        box.config(fg="green")
    # every thing else is black
    else:
        box.insert(0, f"{value}")
        box.config(fg="black")
## confingure window and its boxes
def configure_window( root ):

    root.columnconfigure(2 , weight = 1)
    entry_boxes = [] 

    ## iterate through needed variables and add a label and a box
    ## add entry_boxes for later
    for index, value in enumerate(needed_values):
        valueLabel = tk.Label(root , 
                       text = value , 
                       bg='white')
    
        valueLabel.grid(row = index , 
                 column = 0 , 
                 padx = (10,5) ,
                 pady = (3,3) , 
                sticky = "e")
        valueEntry = tk.Entry(root , 
                       highlightthickness=1 , 
                       width=15,
                       highlightbackground= 'black' , 
                       highlightcolor= 'black', 
                       relief='flat'
                       )
        valueEntry.grid(row = index , 
                 column = 1 ,  
                 padx = (5,10) , 
                 pady = (3,3) , 
                 sticky = "w")
        entry_boxes.append(valueEntry)
    return entry_boxes

def app_main():
    ## run sensor first
    sensors = IPMI_sensors()
    ## Create the main windows
    appID = 'appliedmaterials.PSUreader.GUI.1'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appID)
    root = tk.Tk()
    root.title("AMAT PSU reader")
    root.iconbitmap("pictures\\applied_materials.ico")
    root.geometry("180x180")
    root.configure(bg='white')
    ## Create the text boxes and recieve them back
    value_boxes = configure_window(root)
    def update_data():
        # delete the data in the box first
        for box in value_boxes:
            box.delete(0, tk.END)

        ## update boxes with correct data
        data_to_entry( value_boxes[0]  , f"{sensors.vol5v}V")
        data_to_entry( value_boxes[1]  , f"{sensors.vol3v3}V")
        data_to_entry( value_boxes[2]  , f"{sensors.vol12v}V")
        data_to_entry( value_boxes[3]  , f"{sensors.temp}\u00b0C")
        data_to_entry( value_boxes[4]  , f"{sensors.psu1}")
        data_to_entry( value_boxes[5]  , f"{sensors.psu2}")

        ## refresh the window and the sensors
        sensors.refresh()
        root.after( 1000 , update_data )

    update_data()
    root.mainloop()