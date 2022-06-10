# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line
height_1= float(height)
weight_1 = float(weight)

Bmi= round(weight_1 / height_1**2)
print('Your Bmi is: ' + str(Bmi))


if Bmi < 18.5:
 print("Underweight")

elif Bmi >= 18.5 and Bmi < 25:
 print('Normal weight')

elif Bmi >=25 and Bmi < 30:
 print('Overweight')
  
elif Bmi >=30:
 print('Obese')








