import unittest
import password_generator


class password_generator_test(unittest.TestCase):
	password_length = 12

	def test_password_generator_makes_a_password(self):
		new_password = password_generator.generate_password(self.password_length)

		self.assertEquals(len(new_password), self.password_length)

		print(new_password)

if __name__ == '__main__':
	unittest.main(verbosity=2)