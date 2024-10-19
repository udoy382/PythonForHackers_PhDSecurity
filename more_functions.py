"""
def attack(ip, domain):
    print(ip)
    print(f"Target ip is {ip} and {domain}")

ip = "10.10.10.10"
domin = 'google.com'


attack(ip, domin)
"""

# FUNCTION CHALLENGE >

def room_sqft(width, height):
    sqft = f"Room width is ({width}) and room height is ({height}) and room sqft is ({width * height})"

    return sqft

width = int(input("Enter the room width: "))
height = int(input("Enter the room height: "))

print(room_sqft(width, height))