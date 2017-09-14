import unittest
import user
import json
import random


class user_test(unittest.TestCase):
	def test_user_can_be_translated_to_json(self):
		firstname = "firstname" + str(random.random())
		current_user = user.user()
		current_user.firstname = firstname

		returnedjson = json.loads(current_user.get_json().decode('utf-8'))

		self.assertEqual(returnedjson["user"]["firstname"], firstname)


if __name__ == '__main__':
	unittest.main(verbosity=2)
