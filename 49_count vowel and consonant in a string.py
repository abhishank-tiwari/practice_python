#Program to count vowel and consonant in a string
a = input("Enter your name : ")
vowel = 0
cons = 0
			
for i in range(0,len(a)):
	if (a[i]!= ' '):
		if(a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u" or a[i]=="A" or a[i]=="E" or a[i]=="I" or a[i]=="O" or a[i]=="U"):
			vowel = vowel + 1
		else:
			cons = cons + 1

			
print("Total Vowel=",vowel)
print("Total Consonents = ",cons)