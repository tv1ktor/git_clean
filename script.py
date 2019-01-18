import subprocess
from sys import exit


def init_safe_branch_clean(branches):
	PIPE = subprocess.PIPE
	
	for branch in branches:
		deleted_branch = subprocess.Popen(['git', 'branch', '-d', branch], stdout=PIPE, stderr=PIPE, text=True)
		stdoutput, stderroutput = deleted_branch.communicate()
		print(stdoutput)
		print(stderroutput)
		exit()





