
import sys

num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

if len(num1) > len(num2):
	print ('False')
	sys.exit(0)
# ******************************
# Make your Code
# ******************************

sequenceCounter = 0

for n in num2:
    # checks if the subset is found or not
    if sequenceCounter == len(num1):
        break

    if n == num1[sequenceCounter]:
        sequenceCounter += 1
    else:
        sequenceCounter = 0


if sequenceCounter == len(num1):
    print(True)
else:
    print(False)
    
# print ('True') or ('False')
