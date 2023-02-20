student = {
  "name" : "Jaka",
  "address" : "Jakarta",
}

try:
  print(student)
except NameError:
  print("stdent variable is not defined")
except:
  print("An error occured!")
else:
  print("Script runs succesfully!")
