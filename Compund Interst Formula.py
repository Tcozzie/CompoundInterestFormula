rate=float(input("Annual rate of interest as a decimal. Example (0.043)\n"))
years=float(input("Number of years\n"))
timesCompounded=float(input("Number of times the interest is compounded per year\n"))
initialAmount=float(input("Initial amount borrowed or deposited\n$"))


rN=rate/timesCompounded
rN=1+rN
nT=timesCompounded*years
rN=rN**nT
answer=initialAmount*rN
finalAnswer=str(format(answer,".2f"))
print("$"+finalAnswer)

