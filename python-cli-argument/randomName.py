import argparse
import random

name_list = [
	"Ilham", "Intan", "Anwar", "Sri", "Indah",
	"Annisa", "Faisa", "Rahman", "Akbar", "Zakaria"
]

parser = argparse.ArgumentParser(
	description = "Generate random names"
)

parser.add_argument(
	"-n1", "--number1",
	metavar = "number",
	help = "numbers to be displayed | max = 10",
	required = True
)

parser.parse_args()
args = parser.parse_args()

# convert number argument into integer
number_arg = int(args.number)

# shuffle names in list
random.shuffle(name_list)

# get names for specific range
name_range = name_list[0:number_arg]

# display ranged names
for name in name_range:
	print(name)
