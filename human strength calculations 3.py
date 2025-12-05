# cSC: Updated human input part
## Strength Logic

name = input('name: ')

gender_change_factor = 1.75
life_expectancy_in_years = 125
year_to_seconds = 365.25*24*60*60

bh_male_in_cm = float(input('Bodyheight in cm: '))
age_in_years = float(input('Age in years: '))

life_expectancy_in_seconds = life_expectancy_in_years * year_to_seconds
age_in_seconds = age_in_years * year_to_seconds

bh_female_in_cm = bh_male_in_cm / gender_change_factor

'daily_energy_need_male_in_kj = bh_male_in_cm - 50kg/cm * 125kJ/kg'

daily_energy_need_male_in_kj = (bh_male_in_cm - 50) * 125

power_male_watt_per_seconds = daily_energy_need_male_in_kj / 86.4

robustness = power_male_watt_per_seconds / (life_expectancy_in_seconds - age_in_seconds)

current_capital = float(input('current capital [€]: '))
yearly_income = float(input('current yearly income [€]: '))

money = current_capital + yearly_income * ((life_expectancy_in_seconds - age_in_seconds)/year_to_seconds)

strength_i = robustness / money

print('--------------')
print('Strength of',name,'is:\n\n',strength_i,'W/s^2€')

## storing calculations



'''
### nikola vukojevic

4.375 W/s
1.577.880.000 s

0,000002772708 W/s2 = 2.772708 * 10^-6 W/s2 = 2.772708 mW/s2 = 2.77 mW/s2

806.891,875 € = 806.90 k€

3.43628e-12 W/s2€ = 3.43628 * 10^-12 W/s2€  = 3.44 pW/s^2€

St_more > St_less

### christine lagarde 

1.537,698412698413 wps
315.576.000s

0,000004872672233 wps2
50000000000€
270000000€

9,746e-17 = 975 fW/s^2€
0,000000000000018 = 0.1805 fW/s^2€ = 180.5 aW/s^2€

M of 1,025641025641026e12 € missing for getting 1 St

nachbarn lu 155cm paar

6.721,230158730159 wps
1.293.861.600 s

0,000005194705523 wps2
723.836,75 €

0,000000000007177 = 7.18 pW/s^2€

'''

## Strength Equalizer
### Money Exchange @ Fixed Robustness 
'''
avg: ordinary arithmetic mean (uniform distribution)
'''

'''St_avg = sum(strength_i) / n
M_i = R_i / St_avg'''

'Based on the given robustness R_i give the corresponding money M_i to it.'

