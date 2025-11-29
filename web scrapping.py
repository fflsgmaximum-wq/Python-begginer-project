import requests
from bs4 import BeautifulSoup

# Woh URL jahan se data nikalna hai
URL = "https://en.wikipedia.org/wiki/India"

print("🔍 Website se data nikala ja raha hai...")

try:
    # Website ko kholne ki request bhejna (requests library ka kaam)
    page = requests.get(URL)
    
    # BeautifulSoup se page ko padhne layak banana
    soup = BeautifulSoup(page.content, "html.parser")
    
    # Page ka Title nikalna
    title = soup.find(id="firstHeading").text
    
    print("---------------------------------")
    print("✅ Success! Website ka Title mila:")
    print(f"TITLE: {title}")
    print("---------------------------------")

except Exception as e:
    print("❌ ERROR: Check karein ki aapka internet chalu hai ya nahi.")
