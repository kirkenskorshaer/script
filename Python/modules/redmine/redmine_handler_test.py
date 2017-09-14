import unittest
import redmine_handler
import random
import user
import urllib


class redmine_handler_test(unittest.TestCase):
	def test_class_can_be_instantiated(self):
		store = ""
		url = "url " + str(random.random())
		key = "key " + str(random.random())
		handler = redmine_handler.redmine_handler(store, url, key)

		self.assertEqual(url, handler.url)
		self.assertEqual(key, handler.key)

	def test_exception_for_random_keys(self):
		handler = self.arrange_handler()
		new_user = self.arrange_user()

		with self.assertRaises(urllib.error.URLError):
			handler.create_user(new_user, True)

	def test_create_user_will_not_create_user_if_is_real_is_false(self):
		handler = self.arrange_handler()
		new_user = self.arrange_user()

		handler.create_user(new_user, False)

	def arrange_handler(self):
		store = ""
		url = "https://support.kirkenskorshaer.dk/redmine"
		key = "key " + str(random.random())
		handler = redmine_handler.redmine_handler(store, url, key)
		return handler

	def arrange_user(self):
		new_user = user.user()
		new_user.firstname = "test firstname " + str(random.random())
		new_user.lastname = "test lastname " + str(random.random())
		new_user.login = "test login " + str(random.random())
		new_user.mail = "test_" + str(random.random()) + "@korsnet.dk"
		new_user.password = "test password"
		return new_user


if __name__ == '__main__':
	unittest.main(verbosity=2)
