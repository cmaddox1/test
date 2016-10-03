w8t=int(input('How much do you weigh?'))
ht=int(input('How tall are you, in inches?'))
bmi = ((w8t/(ht**2))*703)

print('Your BMI is:')
print(bmi)

if bmi>=30:
    print('FATTY')
elif bmi>=25:
    print('HIT THE GYM')
elif bmi>=18.5:
    print('you gucci bro')
else: 
    print('eat a donut!')


