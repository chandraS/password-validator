# -*- coding: utf-8 -*-

import argparse
import sys
import os


from password_validator.tries import add, search, Node
from password_validator.const import *

def build_trie(root):
	"""
	This method takes a root paramater from where the trie can be built.
	filepath is a mandatory argument to provide location of weak password.
	Trie will be built on the weak password list
	:param root: trie root
	"""
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

	with open(password_file, "r", encoding='utf-8') as f:
		lines = f.readlines()

		for line in lines:
			add(root, line.strip())

def not_ascii_check(text):
	"""
	check for non ascii character in string
	:param text: word to compare non ascii character
	:return: boolean, true if non ascii character in string
	"""
	if not all(ord(c) < UPPER_ASCII_CODE and ord(c) > LOWER_ASCII_CODE for c in text):
		print(''.join([c if ord(c) < UPPER_ASCII_CODE and ord(c) > LOWER_ASCII_CODE
					   else '*' for c in text]) + '-> INVALID_CHARACTERS')
		return True

	return False


def min_password_check(text):
	"""
	check for minimum length for password
	:param text:  word to check for minimum length
	:return: boolean, true if password fails for minimun length criteria
	"""
	if len(text) < MIN_PASSWORD_LENGTH:
		print('{} --> TOO_SHORT'.format(text))
		return True

	return False


def max_password_check(text):
	"""
	check for maximum length for password
	:param text:  word to check for maximum length
	:return: boolean, true if password fails for maximum length criteria
	"""
	if len(text) > MAX_PASSWORD_LENGTH:
		print('{} --> TOO_LONG'.format(text))
		return True

	return False


def weak_password_check(root, text):
	"""
	compare user input password with weak password file
	:param root: starting trie root from where search will start
	:param text: word to check for common password
	:return: boolean, true if text is found in common password file
	"""
	if search(root, text):
		print('{} -> TOO_COMMON'.format(text))
		return True

	return False

def search_trie(root):
	"""
	This method takes user input from stdin and loop through all the passwords
	provided by the user. It compares each password with the specified rules and
	provide a list of weak/common passwords to the console
	:param root: trie root
	"""

	for line in sys.stdin:
		text = line.strip()

		if not_ascii_check(text):
			continue

		elif min_password_check(text):
			continue

		elif max_password_check(text):
			continue

		else: weak_password_check(root, text)


def main():

	# create root for trie
	root = Node('*')

	build_trie(root)
	search_trie(root)


if __name__ == "__main__":
	main()
