import random


def generate_password(n=6):
	characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*_"
	password = ''.join(random.choice(characters) for i in range(n))
	
	return password
if __name__ == '__main__':
    print('запущен модуль')
    password = generate_password()
    print(password)