import random
import string

# Function 1: Strong Password Generator
def generate_strong_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Function 2: Number ko double karna
def double_number(num):
    return num * 2

# Function 3: Greeting
def developer_greeting(name):
    return f"Hello, Senior Developer {name}! Your code is modular."
