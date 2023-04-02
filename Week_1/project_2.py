# Reading principal amount, rate and time
P = float(input('Enter principal: '))
t = float(input('Enter time: '))
R = float(input('Enter rate: '))
n = float(input('Enter the number of times the interest compounds each year: '))

# Calcualtion
A = P * ((1 + (R/n)) ** (n * t))

# Displaying result
print('Compound interest is: %f' %(A))