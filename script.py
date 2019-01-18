import subprocess
import progressbar
from sys import exit
from time import sleep


def init_safe_branch_clean(branches):
	remaining_branches = []
	PIPE = subprocess.PIPE
	bar = progressbar.ProgressBar(maxval=len(branches), \
		widgets=[progressbar.Bar('|', '[', ']'), ' ', progressbar.Percentage()])
	
	bar.start()
	
	for branch in branches:
		deleted_branch = subprocess.Popen(['git', 'branch', '-d', branch], stdout=PIPE, stderr=PIPE, text=True)
		stdoutput, stderroutput = deleted_branch.communicate()
		bar.update(i+1)
		sleep(0.1)
		if stderroutput:
			remaining_branches.push(deleted_branch)
			continue

	bar.finish()
	exit()
