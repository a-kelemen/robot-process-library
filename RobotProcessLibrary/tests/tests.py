#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, generators, print_function, unicode_literals

import unittest
import os

from EmailProcessLibrary.emailmodule.keywords.exception import *
from EmailProcessLibrary import EmailProcessLibrary

# TODO test email cim
# TODO normalis fajok
class TestReaderKeywords(unittest.TestCase):

	def __init__(self, *args, **kwargs):
		super(TestReaderKeywords, self).__init__(*args, **kwargs)
		self.emailLib = EmailProcessLibrary()

	@classmethod
	def setUpClass(cls):
		test_dir = os.path.dirname(__file__)
		save_folder = os.path.join(test_dir, 'save_folder')
		saved_files = os.listdir(save_folder)
		for f in test_dir:
			if f.endswith(".png"):
				os.remove(os.path.join(test_dir, f))
		for f in saved_files:
			os.remove(os.path.join(save_folder, f))

	def test_read_email_last(self):
		"""Read Last Received Email"""
		mail = self.emailLib.read_last_received_email()
		self.assertIsNotNone(mail)

	def test_read_email_from(self):
		"""Read Last Email From"""
		mail = self.emailLib.read_last_email_from("kelemenandras11@outlook.com")
		self.assertIsNotNone(mail)

	def test_read_email_from_non_existing(self):
		"""Read Last Email From"""
		mail = self.emailLib.read_last_email_from("nincsilyen@outlook.com")
		self.assertIsNone(mail)

	def test_last_received_subject_should_be(self):
		"""Last Received Email Should Be"""
		self.emailLib.last_received_subject_should_be("ketcsatolmany")

	def test_last_received_subject_should_be_non_existing(self):
		"""Last Received Email Should Be"""
		with self.assertRaises(AssertionError):
			self.emailLib.last_received_subject_should_be("xyzzy")

	def test_get_email_non_existing(self):
		"""Get Email"""
		mail = self.emailLib.get_email("asd", "asd", "2019.01.01", None)
		self.assertIsNone(mail)

	def test_get_email_non_existing_2(self):
		"""Get Email"""
		mail = self.emailLib.get_email("asd", "asd", "2000.01.01", "2019.01.01")
		self.assertIsNone(mail)

	def test_get_email_between_dates(self):
		"""Get Email"""
		mail = self.emailLib.get_email("kelemenandras11@outlook.com", "minta", "2019.02.20", "2019.02.27")
		self.assertIsNotNone(mail)

	def test_save_attachment_given_folder(self):
		"""Save Attachments"""
		mail = self.emailLib.get_email("kelemenandras11@outlook.com", "csatolmany", "2019.02.27", "2019.02.27")
		self.assertIsNotNone(mail)
		#print(os.path.dirname(__file__))
		self.emailLib.save_attachments(mail, "save_folder")
		save_folder = os.path.join(os.path.dirname(__file__), "save_folder")
		saved_attachment = os.path.join(save_folder, "Untitled Diagram.png")
		self.assertTrue(os.path.isfile(saved_attachment))

	def test_save_attachment_save_to_default(self):
		"""Save Attachments"""
		mail = self.emailLib.get_email("kelemenandras11@outlook.com", "csatolmany", "2019.02.27", "2019.02.27")
		self.assertIsNotNone(mail)
		self.emailLib.save_attachments(mail)
		save_folder = os.path.dirname(__file__)
		saved_attachment = os.path.join(save_folder, "Untitled Diagram.png")
		self.assertTrue(os.path.isfile(saved_attachment))

	def test_save_attachment_non_existing_folder(self):
		"""Save Attachments"""
		mail = self.emailLib.get_email("kelemenandras11@outlook.com", "csatolmany", "2019.02.27", "2019.02.27")
		self.assertIsNotNone(mail)
		with self.assertRaises(DirectoryNotFoundException):
			self.emailLib.save_attachments(mail, "no//default_")

	def test_save_attachment_multiple(self):
		"""Save Attachments"""
		mail = self.emailLib.get_email("kelemenandras11@outlook.com", "ketcsatolmany", "2019.02.27", "2019.02.27")
		self.assertIsNotNone(mail)
		self.emailLib.save_attachments(mail, "..//tests//save_folder")
		save_folder = os.path.join(os.path.dirname(__file__), "save_folder")
		saved_attachment_a = os.path.join(save_folder, "a.txt")
		saved_attachment_b = os.path.join(save_folder, "b.txt")
		a_isfile = os.path.isfile(saved_attachment_a)
		b_isfile = os.path.isfile(saved_attachment_b)
		self.assertTrue(a_isfile and b_isfile)

	def test_save_attachment_no_file(self):
		"""Save Attachments"""
		mail = self.emailLib.get_email("kelemenandras11@outlook.com", "minta", "2019.01.01", "2019.02.27")
		self.assertIsNotNone(mail)
		self.emailLib.save_attachments(mail, "..//tests//save_folder")

	def test_get_email_text(self):
		"""Get Email Text"""
		mail = self.emailLib.get_email("kelemenandras11@outlook.com", "ketcsatolmany", "2019.02.27", "2019.02.27")
		mail_text = "".join(self.emailLib.get_email_text(mail))
		self.assertIn("szia", mail_text)

	def test_get_email_subject(self):
		"""Get Email Subject"""
		mail = self.emailLib.get_email("kelemenandras11@outlook.com", "ketcsatolmany", "2019.02.27", "2019.02.27")
		mail_subject = self.emailLib.get_email_subject(mail)
		self.assertEqual("ketcsatolmany", mail_subject)

	def test_get_email_time(self):
		"""Get Email Time"""
		mail = self.emailLib.get_email("kelemenandras11@outlook.com", "ketcsatolmany", "2019.02.27", "2019.02.27")
		mail_time = self.emailLib.get_email_time(mail)
		self.assertIn(str(mail_time), ["02/27/19 11:29:33", "2019-02-27 11:29:33+00:00"])

	def test_get_email_sender(self):
		"""Get Email Sender"""
		mail = self.emailLib.get_email("kelemenandras11@outlook.com", "ketcsatolmany", "2019.02.27", "2019.02.27")
		mail_sender = self.emailLib.get_email_sender(mail)
		self.assertEqual("kelemenandras11@outlook.com", mail_sender)


class TestLoginKeywords(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(TestLoginKeywords, self).__init__(*args, **kwargs)
		self.emailLib = EmailProcessLibrary()

	def test_should_be_logged_in_to_outlook(self):
		"""Should Be Logged In To Outlook"""
		self.emailLib.should_be_logged_in_to_outlook("kelemenandras11@outlook.com")

	def test_should_be_logged_in_to_outlook_wrong_email(self):
		"""Should Be Logged In To Outlook"""
		with self.assertRaises(OutlookException):
			self.emailLib.should_be_logged_in_to_outlook("wrongaddress@outlook.com")


if __name__ == '__main__':
	unittest.main()
