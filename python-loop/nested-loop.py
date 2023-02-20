# nested loop

# for example
# we have fruit list
# and color list

# we want to text-combine
# each color with each fruit

fruits = ["Apple", "Banana", "Cherry"]
colors = ["Green", "Red", "Yellow"]

for color in colors:
	for fruit in fruits:
		print(f"{color} {fruit}")

# It will print each color
# for each fruit name