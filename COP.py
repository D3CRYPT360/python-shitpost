# Bottle stuff
class Bottle:

    # Gets called everytime Bottle() is used
    def __init__(self, height, volume, recvcode):
        self.height = height
        self.volume = volume
        self.recvcode = recvcode


height = "50cm"
volume = "25l"
recvcode = "2"

bottle = Bottle(height=height, volume=volume, recvcode=recvcode)

# print(f"The height of the bottle is {bottle.height}, the bottle can store upto {bottle.volume}. The bottle can be used {bottle.recvcode} times")

# Even or odd checker
class eo:

    def __init__(self, num):
        self.num = int(num)

    def eocheck(self):
        if self.num % 2 == 0:
            return f"{self.num} Is an even number"
        else:
            return f"{self.num} Is an odd number"

for x in range(1,51):
    num = x
    # print(eo(num).eocheck())

class pass_or_fail:

    def __init__(self, grade):
        self.grade = int(grade)

    def pof(self):
        if self.grade >= 95:
            return "A*"
        elif self.grade >= 90:
            return "A"
        elif self.grade >= 75:
            return "B"

        elif self.grade >= 50:
            return "C"
        else:
            return "Failed"

grade = input("Enter student grade: ")
pof = pass_or_fail(grade=grade)

print(pof.pof())