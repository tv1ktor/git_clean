import subprocess
import progressbar
from sys import exit
from time import sleep
import pdb 


def init_safe_branch_clean(branches):
	pdb.set_trace()
	failed_branches = []
	PIPE = subprocess.PIPE
	bar = progressbar.ProgressBar(maxval=len(branches), \
		widgets=[progressbar.Bar('|', '[', ']'), ' ', progressbar.Percentage()])
	
	bar.start()
	
	finished = 0
	for branch in branches:
		print(branch)
		print(finished)
		deleted_branch = subprocess.Popen(['git', 'branch', '-d', branch], stdout=PIPE, stderr=PIPE, text=True)
		stdoutput, stderroutput = deleted_branch.communicate()
		finished += 1
		bar.update(finished)
		if stderroutput:
			failed_branches.append(deleted_branch)
			continue

	bar.finish()

	remaining = len(failed_branches)
	print(' Total cleaned: {}\n Active branches remaining: {}'.format(finished-remaining, remaining+1))
	exit()
