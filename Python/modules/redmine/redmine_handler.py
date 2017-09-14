import json
import urllib.request
import ssl


class redmine_handler:
	url = ""
	key = ""
	ssl_context = ""

	def __init__(self, certificate_store, url, key):
		self.url = url
		self.key = key
		if certificate_store != "":
			self.ssl_context = ssl.SSLContext()
			self.ssl_context.load_verify_locations(capath=certificate_store)

	def create_user(self, user_to_send, is_real):
		params = user_to_send.get_json()
		request = urllib.request.Request(self.url + '/users.json', data=params, headers={'content-type': 'application/json'})
		request.add_header("X-Redmine-API-Key", self.key)
		try:
			if is_real is True:
				response = urllib.request.urlopen(request, context=self.ssl_context)
				created_user = json.loads(response.read())
				user_to_send.user_id = created_user["user"]["id"]
			else:
				print("test sending user: " + user_to_send.firstname)
			# print("created user: " + user_to_send.mail + " with id: " + str(user_to_send.user_id))
		except urllib.error.HTTPError as error:
			print(error)
			errorfile = open("create_error.html", "w")
			errorfile.write(error.read().decode("utf-8"))
			errorfile.close()

	def add_user_to_group(self, user_id_to_add, group_to_add_user_to):
		params = json.dumps({'user_id': user_id_to_add}).encode('utf8')
		request = urllib.request.Request(self.url + '/groups/' + group_to_add_user_to + '/users.json', data=params, headers={'content-type': 'application/json'})
		request.add_header("X-Redmine-API-Key", self.key)
		try:
			urllib.request.urlopen(request, context=self.ssl_context)
		except urllib.error.HTTPError as error:
			print(error)
			errorfile = open("add_to_group_error.html", "w")
			errorfile.write(error.read().decode("utf-8"))
			errorfile.close()
