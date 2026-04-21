import pandas as pd
import time
import csv

# 1.0 input
datetime = time.localtime()
set = input('describe the set: ')
energy = float(input('energy: [kJ] '))
money = float(input('price or money: [€] '))

age = float(input('lasting duration or age (time): [s] '))
time = float(input('lasting duration (time): [s] '))

# 2.0 tranformation

'''
x1 ... observable
m ... mass
t ... time
d ... distance
M ... Money
v = d/t
a = v/t
F = m*a
W = F * d
P = W / t
E = P * mf1
mf ... modifying factor 1
R = P / t
St = R / M

'''
power = energy/age
robustness = power/time
energy_price = energy/price
power_price = power/price
strength = robustness/price

'''
print('-------------------\n')
print(datetime)
print('-',set)
print('Energy per Money: ',energy_price, 'kJ/€')
print('Power per Money: ',power_price, 'W/s€')
print('Strength: ',strength, 'W/s^2€')

the_strong = 'wheat flour'
'''
print('Strength: ',strength, 'W/s^2€')

# 2.1 updating

data_entry = (datetime,set,strength)
print(data_entry)

# 2.1.1 writing results to a .csv document


# 2.2 storing sets into a pandas dataframe and sorting descending

strength_data = pd.read_csv('strength data.csv')


# 2.3 storing the updated strongest set in the the_strong variable

print(strength_data.head(1))
the_strong = strength_data.head(1)

# 2.4 normalizing and visualizing

# 2.5 normalizing

# 2.6 visualizing


# 3.0 output
print('\n---------\n>',the_strong)
