#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, generators, print_function, unicode_literals

import ExcelProcessLibrary
import EmailProcessLibrary
import OsProcessLibrary
import OcrProcessLibrary


class RobotProcessLibrary(
		ExcelProcessLibrary.ExcelProcessLibrary,
		OsProcessLibrary.OsProcessLibrary,
		EmailProcessLibrary.EmailProcessLibrary,
		OcrProcessLibrary.OcrProcessLibrary):

	__version__ = '0.1.0'

	ROBOT_LIBRARY_SCOPE = 'GLOBAL'
	ROBOT_LIBRARY_VERSION = __version__

	def __init__(self):
		ExcelProcessLibrary.ExcelProcessLibrary.__init__(self)
		OsProcessLibrary.OsProcessLibrary.__init__(self)
		EmailProcessLibrary.EmailProcessLibrary.__init__(self)
		OcrProcessLibrary.OcrProcessLibrary.__init__(self)

	def vvv(self):
		print("RobotProcessLibrary, v" + self.__version__)

