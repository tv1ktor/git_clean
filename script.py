import subprocess
from sys import exit
import constants as const

def init_safe_branch_clean(branches):
	failed_branches = []
	PIPE = subprocess.PIPE
	for branch in branches:
		deleted_branch = subprocess.Popen(['git', 'branch', '-d', branch],
			stdout=PIPE,
			stderr=PIPE,
			text=True
		)
		stdoutput, stderroutput = deleted_branch.communicate()
		finished += 1
		if stderroutput:
			failed_branches.append(deleted_branch)
			continue

	remaining = len(failed_branches)
	print(const.CLEAN_RESULT_MESSAGE.format(len(branches)-remaining, remaining+1))