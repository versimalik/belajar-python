fruits = ("apple","banana","cherry")

# add "jackfruit" into fruits
# fruits.append("jackfruit") will returns error
# convert to list first
fruits_list = list(fruits)
fruits_list.append("jackfruit")
# convert back to tupple
fruits = tuple(fruits_list)
print(fruits)

# change "banana" into "melon"
# fruits[1] = "melon" will return error
# convert to list first
fruits_list = list(fruits)
fruits_list[1] = "melon"
# convert back to tupple
fruits = tuple(fruits_list)
print(fruits)

# remove "apple" from fruits
# fruits.remove("apple") will return error
# convert to list first
fruits_list = list(fruits)
fruits_list.remove("apple")
# convert back to tupple
fruits = tuple(fruits_list)
print(fruits)