import random

possibilities=["BANANA","ROBOT","CHICKEN","NIKHIL","NEPTUNE","GREEN"]
random.shuffle(possibilities)
answer=list(possibilities[1])
#print(answer)
display=[]
display.extend(answer)
for i in range(len(display)):
	display[i] ="_"

	print ("welcome to hang the man!\n")
	print(' '.join(display))
	print("\n\n\n\n")

count=0

while count < len(answer):
	guess=input(" guess a letter")
	guess= guess.upper()
	for i in range(len(answer)):
		if answer [i] == guess:
			display[i]=guess
			count+= 1
	print(' '.join(display))
	print ("\n\n\n\n")

print("you guessed")