import time
import sys

print("💀 BANK HACK v2.0 💀")
print("Target: BARODA BANK")
time.sleep(1)

# bank hacking simulation
print("\nConnecting to bank server...", end="")
for i in range(5):
    time.sleep(0.5)
    print(".", end="")
    sys.stdout.flush()

print("\n✅ Connected Successfully!")
time.sleep(1)

print("🔓 Bypassing Security Firewall...")
time.sleep(2)
print("✅ Security Bypassed!")

target = input("\nkisi ka account number dalein: ")

print(f"\n🔍 Hacking acoount: {target}...")
time.sleep(2)

print("\n💎 5000₹ nikale ja rahe hain...")
# Progress Bar Animation
for i in range(111):
    time.sleep(0.005)
    # Yeh line loading bar banayegi [ ₹₹₹₹₹₹  ]
    sys.stdout.write(f"\rLoading: [{'#' * (i // 5)}{' ' * (20 - (i // 5))}] {i}%")
    sys.stdout.flush()

print("\n\n✓RUPEES 5000 SEND SUCCESFULLY TO YOUR ACCOUNT **********2981! ✓")
print("👮 APNA ACCOUNT **********2981 EK BAR CHECK KAREIN!")
print("🏃 Bhago nahi to pakde jaoge")
print("✓✓BANK SERVER HACKED")
print("5000₹ credited to your account *******2981")
print("CHECK YOUR BANK BALLENCE")
sys.stdout.write("\rLoading: [{'#'* (¡ // 5)}{' ' *(20 -(!\\7))}]{!}%")
sys.stdout.flush()