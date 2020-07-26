import argparse
import sys
import os

from password_validator.tries import add, search, TrieNode


def main():

	# setting name and description of program
	my_parser = argparse.ArgumentParser(prog="password_validator",
										description="Read files and validate password")
	my_parser.add_argument('filepath',
						   metavar='filepath',
						   type=str,
						   help='password file location')

	# Execute parse_args()
	args = my_parser.parse_args()
	password_file = args.filepath

	if not os.path.isfile(password_file):
		raise ValueError('The file specified does not exist. Please provide a valid path.')
		sys.exit()

	# create root for trie
	root = TrieNode('*')

	with open(password_file, "r", encoding='utf-8') as fp:
		lines = fp.readlines()

		for line in lines:
			add(root, line.strip())

	for line in sys.stdin:
		check = line.strip()

		# the length of the encoded word is compared with original word
		# and used to determine whether its a ASCII or not
		if not len(check) == len(check.encode()):
			print(len(check) * '*' + '-> Error: Invalid Charaters')

		elif len(check) < 8:
			print(check + ' -> Error: Too Short')

		elif len(check) > 64:
			print(check + ' Exceeded maximum length allowed. Max allowed length is 64.')

		elif search(root, check):
			print(check + '-> Error: Too Common')


if __name__ == "__main__":
	main()