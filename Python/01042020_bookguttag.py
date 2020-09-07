import pylab

principal = 1000
interestRate = 0.05
interestRateM = 0.05**(1/12)
years = 20
valuesY = []
valuesM = []
months = []
for i in range(years+1):
    valuesY.append(principal)
    principal += principal*interestRate
for i in range((years+1)*12):
    valuesM.append(principal)
    principal += principal*interestRateM
    months.append((i+1)/12)
pylab.figure(1)
pylab.plot(valuesY)
pylab.plot(months, valuesM)
pylab.title('5% growth. compound annually')
pylab.xlabel('years of compounding')
pylab.ylabel('value of principal')
pylab.show()
# pylab.savefig('funciona-mesmo')