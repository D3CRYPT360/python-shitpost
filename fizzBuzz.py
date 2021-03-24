r = []

"""
Rules:
if number is divisible by 3 replace number with Fizz
if number is divisible by 5 replace number with Buzz
if number is divisible by both 5 and 3 replace number with FizzBuzz
"""

for i in range(1,31):
    if i%5 == 0 and i%3 == 0:
        """
        putting it here because if a number is divisible by 3 or 5 and if
        i put `i%x` == 0 here instead of this check it would take that and
        this check will never happen. - note to self, not interesting.
        """
        r.append("FizzBuzz")
    elif i%3 == 0:
        r.append("Fizz")
    elif i%5 == 0:
        r.append("Buzz")
    
    else:
        r.append(i)

print(r)
