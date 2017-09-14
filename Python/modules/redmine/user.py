import json


class user:
	user_id = 0
	login = ""
	firstname = ""
	lastname = ""
	mail = ""
	password = ""
	mail_notification = "only_my_events"
	send_information = "false"

	def get_json_text(self):
		user_info = {
			"user": {
				"login": self.login,
				"firstname": self.firstname,
				"lastname": self.lastname,
				"mail": self.mail,
				"password": self.password,
				"mail_notification": self.mail_notification
			},
			"send_information": self.send_information
		}
		return json.dumps(user_info)

	def get_json(self):
		return self.get_json_text().encode('utf8')
