r = []

"""
Rules:
if number is divisible by 3 replace number with Fizz
if number is divisible by 5 replace number with Buzz
if number is divisible by both 5 and 3 replace number with FizzBuzz
"""

for i in range(1,31): # cuz why not lol
    if i%5 == 0 and i%3 == 0: 
        r.append("FizzBuzz")
    elif i%3 == 0:
        r.append("Fizz")
    elif i%5 == 0:
        r.append("Buzz")
    
    else:
        r.append(i)

print(r)
