# (Computational) Strength Calculator

import pandas as pd
import time
import csv

state1 = 1
while state1 > 0:
	## 1.0 input
	datetime = time.localtime()
	observable = input('describe the observation: ')
	pot_energy = float(input('potential energy / work: [J / Nm] '))
	time_1 = float(input('lasting duration or age (time): [ s] '))
	time_2 = float(input('lasting duration (time): [s] '))
	money = float(input('price or money: (e.g.[€]) '))
	
	## 2.0 transformation
	
	'''
	x1 ... observable
	m ... mass
	t ... time
	r ... position
	M ... money
	v = d/t ... velocity
	a = v/t ... acceleratiom
	F = m*a ... force
	W = F * d = E ...work or energy
	P = W / t ... power
	E = P * mf1 ... energy
	mf ... modifying factor 1
	sR = P / t ... simple robustness
	sSt = sR / M ... simple strength
	sWk = sR / -M = -sSt ... simple weakness
	'''
	power = pot_energy/time_1
	simple_robustness = power/time_2
	energy_price = pot_energy/money
	power_price = power/money
	simple_strength = simple_robustness/money
	simple_weakness = (simple_robustness/money)*(-1)
	
	## 3.0 output
	
	if simple_strength >= 0:
		print('\n------\nSimple Strength: ',simple_strength, 'W/sM or sSt\n------\n')
		state1 = state1 - 1
	else:
		print('\n------\nthis is not a strength, it is a weakness! redo the entry ...\n------\n')
		state1 = state1 + 1

