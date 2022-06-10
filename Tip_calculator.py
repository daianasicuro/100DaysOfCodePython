print('Welcome to the tip calculator!')

Total_bill= float(input('What was the total bill? $'))
Tip_percent= int(input('What percentage tip would you like to give? 10, 12, or 15?'))
Total_people= int(input('How many people to split the bill?'))

Tip_10=(Total_bill / Total_people) * 1.10
Tip_12= (Total_bill / Total_people) * 1.12
Tip_15= (Total_bill / Total_people) * 1.15

if Tip_percent == 10:
  print(f'Each person should pay $ {round( Tip_10, 2)}')

elif Tip_percent == 12:
  print(f'Each person should pay $ {round( Tip_12, 2)}')

elif Tip_percent == 15:
  print(f'Each person should pay $ {round(Tip_15, 2)}')