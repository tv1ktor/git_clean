#!/usr/bin/env python3
from sys import exit
import subprocess
import re 
import constants as const

# Fetch and display all branches
PIPE = subprocess.PIPE

git_status = subprocess.Popen(['git', 'status'], stdout=PIPE, stderr=PIPE, text=True)
status_output, status_error = git_status.communicate()

git_branch = subprocess.Popen(['git', 'branch'], stdout=PIPE, stderr=PIPE, text=True)
branch_output, branch_error = git_branch.communicate()

if status_error:
	print(const.GIT_STATUS_ERROR.format(status_error))
	exit()
elif branch_error:
	print(const.GIT_BRANCH_ERROR.format(output_error))
	exit()


def print_found_branches(branch_list, branch_current):
	for branch in branch_list:
		if branch in ('master', branch_current):
			print("\033[92m" + branch, "(safe)\033[0m")
		else:
			print(branch)
	print(const.SEARCH_RESULT_MESSAGE.format(len(branch_list)))


def begin_program_looping(branch_list, branch_current):
	while True:
		print(const.BEGIN_CLEAN_PROMPT)
		cmd = input()
		if cmd == 'y':
			from script import init_safe_branch_clean
			branch_list.remove('master')
			if 'master' != branch_current:
				branch_list.remove(branch_current)
			return init_safe_branch_clean(branch_list)
		elif cmd == 'n':
			raise KeyboardInterrupt
		else: 
			print(const.WRONG_CMD_MESSAGE)


def main():
	branches = re.split(r"\s+|\n|[\s\*]", branch_output)
	branches = list(filter(None, branches))
	current_br = status_output.split('\n')[0].split(' ')[2]
	print(current_br)
	print_found_branches(branches, current_br)
	try:
		begin_program_looping(branches, current_br)
	except KeyboardInterrupt as error:
		print(const.EXIT_MESSAGE)
		exit()
	# Check for additional commands here later


if __name__ == "__main__":
	main()


	
