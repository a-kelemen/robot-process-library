# coding: utf-8from __future__ import absolute_import, division, generators, nested_scopes, print_function, unicode_literals, with_statementimport sysimport osprocess_file = open(sys.argv[1], 'r')lines = process_file.readlines()process_file.close()for i, line in enumerate(lines):	line = str(line)	try:		line.replace(" ", "").lower()	except UnicodeDecodeError:		continue	if "***processes***" in line.replace(" ", "").lower():		line = "*** Test Cases *** \n#" + line.rstrip("\n") + " _change__" + "\n"		lines[i] = line		breaknew_file_name = "_".join(os.path.splitext(sys.argv[1]))write_file = open(new_file_name, 'w')for line in lines:	write_file.write(str(line))write_file.close()