# coding: utf-8
"""Listener that edits log files"""

from __future__ import absolute_import, division, generators, nested_scopes, print_function, unicode_literals, with_statement
import os
import re


class Process(object):
	ROBOT_LISTENER_API_VERSION = 3

	def __init__(self):
		self.output_source = None

	def output_file(self, path):
		self.output_source = path

	def log_file(self, path):
		log_source = path
		f = open(log_source, 'r')
		filedata = f.readlines()
		f.close()

		f = open(log_source, 'w')
		line_no = 0
		for line in filedata:
			line = str(line)

			#TODO haetekonyan, mert valami csak egyszer van
			try:
				"." in line
			except UnicodeDecodeError:
				f.write(line)
				line_no += 1
				continue
			if "<h2>Test Execution Log</h2>" in line:
				print("csere1", line_no)
				line = line.replace("<h2>Test Execution Log</h2>", "<h2>Process Execution Log</h2>")
			elif 'givenTitle : suiteName + " Test " + type' in line:
				print("csere2", line_no)
				line = line.replace('givenTitle : suiteName + " Test " + type', 'givenTitle : suiteName + " Process " + type')
			elif "Test Statistics" in line:
				print("csere3", line_no)
				line = ""
				filedata[line_no + 1] = ""
				filedata[line_no + 2] = ""
			elif '<span class="label ${status.toLowerCase()}">TEST</span>' in line:
				line = line.replace("TEST", "SUBPROCESS")
				print("csere4", line_no)
			elif '<span class="label ${status.toLowerCase()}">SUITE</span>' in line:
				line = line.replace("SUITE", "PROCESS")
				print("csere5", line_no)

			elif "${critical} critical test," in line:
				line = line.replace("critical test", "process")
				print("csere6", line_no)
			elif "${total} test total," in line:
				line = line.replace("test", "process")
				print("csere7", line_no)
			elif ">Statistics by Suite</th>" in line:
				line = line.replace("Suite", "Process")
				print("csere8", line_no)



			f.write(line)
			line_no += 1

		#newdata = re.sub(r".*\n.*Total Statistics.*\n.*\n", "", filedata)
		#if filedata.find(r".*\r\n.*(Total Statistics).*\r\n.*\r\n") != -1:
		#    print('true')
		#    print(filedata.index(r".*\r\n.*(Total Statistics).*\r\n.*\r\n"))
		#else:
		#    print('false')

		#'<table class="statistics" id="total-stats"><thead><tr>' +
		#'<th class="stats-col-name">Total Statistics</th>' + statHeaders +
		#'</tr></thead></table>' +

		f.close()
		os.remove(self.output_source)

