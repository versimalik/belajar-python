battery_level = "low"


# turning on device process

# checking the battery level
# if battery is low,
# 	do not turn on
# if battery is not low (fair or above)
# 	turn it on

if battery_level == "low":
	print("Your battery is low . . .")
	print("Please, charge the battery")
else:
	print("Device is turning on . . .")

# using 'else' without provide condition
# because 'else' already means,
# opposite condition apart from previous condition

