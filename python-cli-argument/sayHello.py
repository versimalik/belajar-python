import argparse

# create a new Argument Parses object
# type the program description
parser = argparse.ArgumentParser(
		description = 'Just provide your name!'
		)

# add new argument
parser.add_argument('-n', '--name', required = True, help='show hello words to a name')

# parse added arguments
parser.parse_args(['-h'])
args = parser.parse_args()

print(f"Hello, {args.name}! How are you?")

