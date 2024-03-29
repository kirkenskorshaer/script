import modules.redmine.redmine_handler
import modules.redmine.user
import modules.util.file_helper
import modules.util.password_generator
import csv
import sys
import getopt


try:
	options, arguments = getopt.getopt(sys.argv[1:], "k:c:v:t", ["key=", "cert_path=", "verbosity=", "test"])
except getopt.GetoptError:
	print("create_redmine_users -k <key> -c <cert_path> -v <verbosity> -t")
	sys.exit(2)

certificate_path = ""
url = "https://support.kirkenskorshaer.dk/redmine"
key = ""
verbosity = 0
test = False
password_length = 12

for option, argument in options:
	if option in ("-k", "--key"):
		key = argument
	if option in ("-c", "--cert_path"):
		certificate_path = argument
	if option in ("-v", "--verbosity"):
		verbosity = int(argument)
	if option in ("-t", "--test"):
		test = True

bruger_group = "9"
global_redmine_handler = modules.redmine.redmine_handler.redmine_handler(certificate_path, url, key)

file_name = "input.txt"
file_length = modules.util.file_helper.find_file_length(file_name)

current_user_number = 0

with open(file_name) as csvfile:
	user_reader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in user_reader:
		current_user = modules.redmine.user.user()
		current_user.login = row[0]
		current_user.firstname = row[1]
		current_user.lastname = row[2]
		current_user.mail = row[3]
		current_user.password = row[4]
		if current_user.password == "":
			current_user.password = modules.util.password_generator.generate_password(password_length)
		current_user_number += 1
		if test is True:
			print(current_user.get_json_text())
		else:
			global_redmine_handler.create_user(current_user, True)
			global_redmine_handler.add_user_to_group(current_user.user_id, bruger_group)
		if verbosity > 0:
			print(str(round((current_user_number * 100.0) / file_length)) + '% ' + str(current_user_number) + ' / ' + str(file_length))


print("done")
