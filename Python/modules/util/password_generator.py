import random
import string

def generate_password(length):
	return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length))