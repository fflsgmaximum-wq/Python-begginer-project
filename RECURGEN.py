# RECURSION: Function khud ko call karta hai

def factorial(n):
    # Base Case (Rukne ki shart): Agar number 0 ya 1 ho, to ruk jao
    if n == 0 or n == 1:
        return 1
    # Recursive Step: Function khud ko n-1 ke liye wapas call karta hai
    else:
        # Code samjhen: 5! = 5 * factorial(4)
        return n * factorial(n - 1) 

print("🧠 RECURSION CHALLENGE: FACTORIAL 🧠")
print("------------------------------------")
try:
    number = int(input("Kis number ka factorial nikalna hai (e.g., 5): "))
    if number < 0:
        print("❌ Negative number ka factorial nahi nikalta.")
    else:
        result = factorial(number)
        print(f"\n✨ {number}! ka jawab hai: {result}")
        print(f"(Jaise: 5! ka matlab hai 5*4*3*2*1)")
except ValueError:
    print("❌ Kripya sirf number dalein.")
