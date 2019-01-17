#!/usr/bin/env python3
import subprocess

PIPE = subprocess.PIPE

process = subprocess.Popen(['git', 'branch'], stdout=PIPE, stderr=PIPE, text=True)
stdoutput, stderroutput = process.communicate()

