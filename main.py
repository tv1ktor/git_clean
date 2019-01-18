#!/usr/bin/env python3
from sys import exit
import subprocess
import re 

PIPE = subprocess.PIPE
git_brunches = subprocess.Popen(['git', 'branch'], stdout=PIPE, stderr=PIPE, text=True)
stdoutput, stderroutput = git_brunches.communicate()

if stdoutput:
	branches = re.split(r"\s+|\n|[\s\*]", stdoutput)
	branches = list(filter(None, branches))
	print("Found {} branches.".format(len(branches)))

	for branch in branches:
		if branch == 'master':
			print("\033[92m" + branch, "(safe)\033[0m")
		else:
			print(branch)
else:
	print("Output from subprocess not received")
	exit()

try:
	while True:
		command = input('Delete all fully merged branches [y/n]: ')
		if command == 'y':
			from script import init_safe_branch_clean
			branches.remove('master')
			init_safe_branch_clean(branches)
		elif command == 'n':
			raise KeyboardInterrupt
		else: 
			print("Given wrong command.")

except KeyboardInterrupt as error:
	print('Exiting the program...')
	exit()
	
