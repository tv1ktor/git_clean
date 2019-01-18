#!/usr/bin/env python3
from sys import exit
import subprocess
import re 

# Fetch and display all branches
PIPE = subprocess.PIPE
git_query = subprocess.Popen(['git', 'branch'], stdout=PIPE, stderr=PIPE, text=True)
output, output_error = git_query.communicate()

if output:
	branches = re.split(r"\s+|\n|[\s\*]", output)
	branches = list(filter(None, branches))
	for branch in branches:
		if branch == 'master':
			print("\033[92m" + branch, "(safe)\033[0m")
		else:
			print(branch)
	print("<< Found {} branches:".format(len(branches)))
else:
	print("<< Subprocess error: {}".format(output_error))
	exit()

# Receive command and call cleaner function
try:
	while True:
		cmd = input('\n>> Delete all fully merged branches [y/n]: ')
		if cmd == 'y':
			from script import init_safe_branch_clean
			branches.remove('master')
			init_safe_branch_clean(branches)
		elif cmd == 'n':
			raise KeyboardInterrupt
		else: 
			print("<< Wrong command")

except KeyboardInterrupt as error:
	print('<< Exiting the program...')
	exit()
	
