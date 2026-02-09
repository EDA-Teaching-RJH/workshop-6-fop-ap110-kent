#Task 2.1 : system status 
rover_status = {
    "Battery" : 100 , 
    "Heater"  : "off",
    "Camera"  : "Standby"
}

print(rover_status["Battery"])

#Task 2.2: Status Update 

rover_status["Battery"] = 85
rover_status["Heater"] = "On"
rover_status["Speed"] = 5

print(rover_status)

#Task 2.3: The scince log (Nesting)

mission_log = [
    {"Site": "Crater A", "Radiation": "Low", "Water": False},
    {"Site": "Dune B", "Radiation": "High", "Water": True}
]