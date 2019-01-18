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
	
	items_finished = 0
	for branch in branches:
		deleted_branch = subprocess.Popen(['git', 'branch', '-d', branch], stdout=PIPE, stderr=PIPE, text=True)
		stdoutput, stderroutput = deleted_branch.communicate()
		items_finished =+ 1
		bar.update(items_finished)
		sleep(0.1)
		if stderroutput:
			remaining_branches.insert(-1, deleted_branch)
			continue

	bar.finish()

	items_failed = len(remaining_branches)
	print(' Total cleaned: {}\n Active branches remaining: {}'.format(items_finished-items_failed, items_failed))
	exit()
