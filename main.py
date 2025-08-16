import random

l=["stone", "paper", "scissor"]

##########33333

comp=0
userr=0
while comp<5 and userr<5:
	ch = int(input(f"Enter your choice({l}): "))
	user = l[ch-1]
	if user not in l:
		print(f"choose from these options: {l}")
		continue
	a=random.choice(l)
	print(f"Computer choose: {a}")
	if user==a:
		print("Its a tie! ")
	elif (user=="stone" and a== "scissor"):
		print("YOU wins !!!!")
		userr += 1
	elif user=="stone" and a=="paper":
		print("computer wins !!!")
		comp +=1
	elif user=="paper" and a=="stone":
		print("YOU wins !!!")
		userr +=1
	elif user=="paper" and a=="scissor":
		print("computer wins !!!!!")
		comp+=1
	elif user=="scissor" and a=="paper":
		print("YOU wins !!!!")
		userr+=1
	elif user=="scissor" and a=="stone":
		print("computer wins !!!!!")
		comp+=1
	print(f"computer score: {comp} \nuser score: {userr}")
if comp==5 : 
	print("COMPUTER won !!! ")
else :
	print("tu jit gya ladle ") 



