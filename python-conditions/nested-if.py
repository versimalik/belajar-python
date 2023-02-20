age = 18
driver_license = False


# checking age
# then checking driver_license
# if age is teenager yet?
# if yes check driver license
	# if has driver license
	# allow to drive
	# if has no  driver license
	# do not allow to drive
# if not tenager yet
# User not allowed to drive yet

if age > 17:
	print("User is tenager")
	if driver_license == True:
		print("And driving is allowed")
	else:
		print("But driving is not allowed")
else:
	print("User is not yet a tenager")
	print("So driving is not allowed")