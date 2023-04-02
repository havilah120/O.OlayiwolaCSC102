# Reading principal amount, rate and time
P = float(input('Enter principal: '))
T = float(input('Enter time: '))
R = float(input('Enter rate: '))

# Calcualtion
A = P * (1 + ((R/100) * T))

# Displaying result
print('Simple interest is: %f' % (A))
