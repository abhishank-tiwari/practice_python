#Find compound interest
def compound_interest(principle , rate , time):
	Amount = principle*(pow((1+rate/100),time))
	CI = Amount - principle
	print("Compound Interest is :",CI)
	
compound_interest(1000,6.2,2)