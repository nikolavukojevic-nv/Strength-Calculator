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

power_male_watt_per_seconds = daily_energy_need_male_in_kj / age_in_seconds

robustness = power_male_watt_per_seconds / (life_expectancy_in_seconds - age_in_seconds)

current_capital = float(input('current capital [e.g. €]: '))
yearly_income = float(input('current yearly income [e.g. €]: '))

money = current_capital + yearly_income * ((life_expectancy_in_seconds - age_in_seconds)/year_to_seconds)

strength_i = robustness / money

print('--------------')
print('Strength of',name,'is:\n\n',strength_i,'W/sM')

## storing calculations

