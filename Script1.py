#this is a simple python program which takes 3 user inputs from user.
print('Interest Calculator:')

amount = float(input('Principal amount ?'))
roi = float(input('Rate of Interest ?'))
yrs = int(input('Duration (no. of years) ?'))

total = (amount * (1 + (roi*yrs)/100) )
interest = total - amount
print('\nInterest = %0.2f' %interest)
