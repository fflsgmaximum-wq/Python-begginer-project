# File 2: main_app.py ka content
# Import se dusri file ka code use karna
import my_utilitied as utils 
 

print("🚀 Professional Developer Tool 🚀")

# Function ko dusri file se call karna
dev_name = "KHUNI HERE" 
print(utils.developer_greeting(dev_name))

# Password generate karna
new_pass = utils.generate_strong_password(10)
print(f"Generated Password: {new_pass}")

# Math function use karna
result = utils.double_number(150)
print(f"Double of 150 is: {result}")
