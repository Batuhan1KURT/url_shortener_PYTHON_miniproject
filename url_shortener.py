#URL SHORTENER

"""

!!!!       install pyshorteners library with pip with this command -> || pip install pyshorteners ||     !!!!

"""


import pyshorteners

# Get the long URL as input from the user
longer_url = input("Enter the URL: ").strip()

# Function to shorten the URL
def shortener(url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)

# Print the shortened URL
print(shortener(longer_url))