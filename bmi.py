
height = int(input('Please enter your height input feet and inches(whole number): '))
weight = int(input('Please enter your weight input pounds(whole number): '))
bmi = (weight*703)/(height*height)

if bmi <= 18.5:
        print('Your BMI is', bmi,'which means you are underweight.')

elif bmi > 18.5 and bmi < 24.9:
        print('Your BMI is', bmi,'which means you are normal.')

elif bmi > 25 and bmi < 29.9:
        print('Your BMI is', bmi,'which means you are overweight')

elif bmi > 30:
        print('Your BMI is', bmi,'which means you are obese.')

else:
        print('There is an error with your input')
        print('Please check you have entered whole numbers\n'
              'and decimals were asked.')
