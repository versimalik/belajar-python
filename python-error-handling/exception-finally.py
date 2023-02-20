student = {
  "name" : "Jaka",
  "address" : "Jakarta",
}

try:
  print(stdent)
except NameError:
  print("stdent variable is not defined")
except:
  print("An error occured!")
finally:
  print("Script has run!")
  print("The prgram stopped!")
