import random
import string

def password_gen():
    pass_len = 12
    pass_char=string.ascii_letters + string.ascii_uppercase + string.digits + string.punctuation
    password=''.join(random.choice(pass_char) for i in range(pass_len))
    return password
# Password = password_gen()
print("your password is : ",password_gen())