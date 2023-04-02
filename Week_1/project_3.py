# Reading principal amount, rate and time
PMT = float(input('Enter the period of cash payment: '))
R = float(input('Enter rate: '))
t = float(input('Enter time: '))
n = float(input('Enter the number of times the interest compounds each year: '))

# Calcualtion
A = PMT *((((1 + (R/n)) ** (n * t)) - 1 ) / (R / n))

# Displaying result
print('Compound interest is: %f' %(A))