

import random
# print(random.randint(1, 10))  # Random integer between 1 and 10
# print(random.choice(['apple', 'banana', 'cherry']))  # Random choice from a list
# print(random.random())  # Random float between 0.0 and 1.0
# print(random.sample(range(100), 5))  # 5 unique random numbers from 0 to 99


def four_digit_pin():
     """Generate a random four-digit PIN."""
     return f"{random.randint(0, 9999):04}"
print(f"Your four digit otp is {four_digit_pin()}")