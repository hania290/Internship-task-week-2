import random
from datetime import datetime

# Generate a random number between 1 and 100
rand_num = random.randint(1, 100)
print("Random number:", rand_num)

# Get current date and time
now = datetime.now()
print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))
