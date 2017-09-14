import unittest
import file_helper
import os


class file_helper_test(unittest.TestCase):
	filename = "test_tmp.txt"
	filelength = 2

	def test_find_file_length_finds_length_of_a_file(self):
		self.arrange_file()

		file_length = file_helper.find_file_length(self.filename)

		self.assertEquals(self.filelength, file_length)

		os.remove(self.filename)

	def arrange_file(self):
		file = open(self.filename, "w")
		for index in range(self.filelength):
			file.write("line" + str(index) + "\n")
			print(str(index))
		file.close()
		return file
