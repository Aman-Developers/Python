# in this code we are practicing list as well as random module
#for selecting friend for paying the bill randomly

import random
friends = ["Aman", "Rasool","Muzammil", "Shahnawaz", "Arbaz", "Muzzamil"]

selected = random.randint(0,5)

print(f"selectted Person is {friends[selected]}")