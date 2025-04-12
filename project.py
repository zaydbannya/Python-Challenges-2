import random
import string
def generate_random_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))  
    password_list = list(password)
    random.shuffle(password_list)
    shuffled_password = ''.join(password_list)
    return shuffled_password
password_length = int(input("Enter the length of the password: "))
random_password = generate_random_password(password_length)
print("Your random password is:", random_password)