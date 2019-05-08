# coding: utf-8
"""Listener that edits log files"""

from __future__ import absolute_import, division, generators, nested_scopes, print_function, unicode_literals, with_statement
import os


class Process(object):
	ROBOT_LISTENER_API_VERSION = 3

	def __init__(self):
		self.output_source = None

	def output_file(self, path):
		self.output_source = path

	def output_file(self, path):
		self.output_source = path

	def log_file(self, path):
		log_source = path
		f = open(log_source, 'r')
		file_data = f.readlines()
		f.close()

		f = open(log_source, 'w')
		line_no = 0
		for line in file_data:
			line = str(line)

			try:
				"." in line
			except UnicodeDecodeError:
				f.write(line)
				line_no += 1
				continue
			if "<h2>Test Execution Log</h2>" in line:
				line = line.replace("<h2>Test Execution Log</h2>", "<h2>Process Execution Log</h2>")
			elif 'givenTitle : suiteName + " Test " + type' in line:
				line = line.replace('givenTitle : suiteName + " Test " + type', 'givenTitle : suiteName + " Process " + type')
			elif "Test Statistics" in line:
				line = ""
				file_data[line_no + 1] = ""
				file_data[line_no + 2] = ""
			elif '<span class="label ${status.toLowerCase()}">TEST</span>' in line:
				line = line.replace("TEST", "SUBPROCESS")
			elif '<span class="label ${status.toLowerCase()}">SUITE</span>' in line:
				line = line.replace("SUITE", "PROCESS")
			elif "${critical} critical test," in line:
				line = line.replace("critical test", "process")
			elif "${total} test total," in line:
				line = line.replace("test", "process")
			elif ">Statistics by Suite</th>" in line:
				line = line.replace("Suite", "Process")
			elif "window.output" in line and ("_.txt" in line or "_.robot" in line):
				line = line.replace("_.txt", ".txt").replace("_.robot", ".robot")

			f.write(line)
			line_no += 1

		f.close()
		os.remove(self.output_source)

