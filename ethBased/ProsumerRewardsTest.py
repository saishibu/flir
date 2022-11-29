#!usr/bin/python3
#test program to validate reward for prosumers.

#Single Base Tarriff for Prosumers
btp = 2.97

#Slab based tarriff for Consumers
# 0 - 50
# 51 - 100
# 101 - 150
# 151 - 200
# 201 - 251
# 0 - 300
# 0-350
# 0 - 400
# 0 - 500
# >500

btc1 = 3.15 
btc2 = 3.7
btc3 = 4.8
btc4 = 6.4
btc5 = 7.6
btc6 = 5.8
btc7 = 6.6
btc8 = 6.9
btc9 = 7.1
btc10 = 7.9

#number of Prosumers
nP = int(input("No of Prosumers: "))

#number of Consumers
nC = int(input("No of Consumers: "))

#Get Prosumers data
P1gen = int(input("Power generation for P1: "))
P1exp = int(input("Power Export for P1: "))
P1con = P1gen - P1exp
P1Tariff = P1exp * btp
P1PDA = P1con/P1gen
P1 = {"P1gen":P1gen,"P1exp":P1exp,"P1con":P1con,"P1Tariff":P1Tariff,"P1PDA":P1PDA}
print(P1)

P2gen = int(input("Power generation for P2: "))
P2exp = int(input("Power Export for P2: "))
P2con = P2gen - P2exp
P2Tariff = P2exp * btp
P2PDA = P2con/P2gen
P2 = {"P2gen":P2gen,"P2exp":P2exp,"P2con":P2con,"P2Tariff":P2Tariff,"P2PDA":P2PDA}
print(P2)

P3gen = int(input("Power generation for P3: "))
P3exp = int(input("Power Export for P3: "))
P3con = P3gen - P3exp
P3Tariff = P3exp * btp
P3PDA = P3con/P3gen
P3 = {"P3gen":P3gen,"P3exp":P3exp,"P3con":P3con,"P3Tariff":P3Tariff,"P3PDA":P3PDA}
print(P3)

P4gen = int(input("Power generation for P4: "))
P4exp = int(input("Power Export for P4: "))
P4con = P4gen - P4exp
P4Tariff = P4exp * btp
P4PDA = P4con/P4gen
P4 = {"P4gen":P4gen,"P4exp":P4exp,"P4con":P4con,"P4Tariff":P4Tariff,"P4PDA":P4PDA}
print(P4)

P5gen = int(input("Power generation for P5: "))
P5exp = int(input("Power Export for P5: "))
P5con = P5gen - P5exp
P5Tariff = P5exp * btp
P5PDA = P5con/P5gen
P5 = {"P5gen":P5gen,"P5exp":P5exp,"P5con":P5con,"P5Tariff":P5Tariff,"P5PDA":P5PDA}
print(P5)

#Get Consumer data

C1imp = int(input("Power import for C1: "))

if (C1imp <= 250):
	if (C1imp <= 50):
		C1Tariff = C1imp * btc1
	elif (C1imp >50 and C1imp <=100):
		C1Tariff = 50 * btc1 + (C1imp - 50) * btc2
	elif (C1imp >100 and C1imp <=150):
		C1Tariff = 50 * btc1 + 50 * btc2 + (C1imp - 100) * btc3
	elif (C1imp >150 and C1imp <=200):
		C1Tariff = 50 * btc1 + 50 * btc2 + 50 * btc3 + (C1imp - 150) * btc4
	elif (C1imp >200 and C1imp <=250):
		C1Tariff = 50 * btc1 + 50 * btc2 + 50 * btc3 + 50 * btc4 + (C1imp - 200) * btc5
elif (C1imp > 250 and C1imp <=300):
	C1Tariff = C1imp * btc6
elif (C1imp > 300 and C1imp <=350):
	C1Tariff = C1imp * btc7
elif (C1imp > 350 and C1imp <=400):
	C1Tariff = C1imp * btc8
elif (C1imp > 400 and C1imp <=500):
	C1Tariff = C1imp * btc9
elif (C1imp > 500):
	C1Tariff = C1imp * btc10

print("Tarriff for C1: "+ str(C1Tariff))
C1 = {"C1imp":C1imp,"C1Tariff":C1Tariff}

C2imp = int(input("Power import for C2: "))
if (C2imp <= 250):
	if (C2imp <= 50):
		C2Tariff = C2imp * btc1
	elif (C2imp >50 and C2imp <= 100):
		C2Tariff = 50 * btc1 + (C2imp - 50) * btc2
	elif (C2imp >100 and C2imp <= 150):
		C2Tariff = 50 * btc1 + 50 * btc2 + (C2imp - 100) * btc3
	elif (C2imp >150 and C2imp <= 200):
		C2Tariff = 50 * btc1 + 50 * btc2 + 50 * btc3 + (C2imp - 150) * btc4
	elif (C2imp >200 and C2imp <= 250):
		C2Tariff = 50 * btc1 + 50 * btc2 + 50 * btc3 + 50 * btc4 + (C2imp - 200) * btc5
elif (C2imp > 250 and C2imp <= 300):
	C2Tariff = C2imp * btc6
elif (C2imp > 300 and C2imp <= 350):
	C2Tariff = C2imp * btc7
elif (C2imp > 350 and C2imp <= 400):
	C2Tariff = C2imp * btc8
elif (C2imp > 400 and C2imp <= 500):
	C2Tariff = C2imp * btc9
elif (C2imp > 500):
	C2Tariff = C2imp * btc10

print("Tariff for C2: "+ str(C2Tariff))
C2 = {"C2imp":C2imp,"C2Tariff":C2Tariff}

C3imp = int(input("Power import for C3: "))
if (C3imp <= 250):
	if (C3imp <= 50):
		C3Tariff = C3imp * btc1
	elif (C3imp >50 and C3imp <=100):
		C3Tariff = 50 * btc1 + (C3imp - 50) * btc2
	elif (C3imp >100 and C3imp <=150):
		C3Tariff = 50 * btc1 + 50 * btc2 + (C3imp - 100) * btc3
	elif (C3imp >150 and C3imp <=200):
		C3Tariff = 50 * btc1 + 50 * btc2 + 50 * btc3 + (C3imp - 150) * btc4
	elif (C3imp >200 and C3imp <=250):
		C3Tariff = 50 * btc1 + 50 * btc2 + 50 * btc3 + 50 * btc4 + (C3imp - 200) * btc5
elif (C3imp > 250 and C3imp <=300):
	C3Tariff = C3imp * btc6
elif (C3imp > 300 and C3imp <=350):
	C3Tariff = C3imp * btc7
elif (C3imp > 350 and C3imp <=400):
	C3Tariff = C3imp * btc8
elif (C3imp > 400 and C3imp <=500):
	C3Tariff = C3imp * btc9
elif (C3imp > 500):
	C3Tariff = C3imp * btc10

print("Tarriff for C3: "+ str(C3Tariff))
C3 = {"C3imp":C3imp,"C3Tariff":C3Tariff}


print("\nComputing Power Balance")

PD = C1imp + C2imp + C3imp
PA = P1exp + P2exp + P3exp + P4exp + P5exp

PDA = PA/PD

print ("Power Availability: " + str(PA))
print ("Power Demand: " + str(PD))
print ("PDA: " + str(PDA))

PBal = PD - PA

CostTBal = PBal * btp
TotalConsumerCost = C1Tariff + C2Tariff + C3Tariff
TotalProsumerCostNoReward = PA*btp

if (PDA > 0.99):
	print("\nLess Demand")
elif (PDA < 0.5):
	print ("\nNo suitable Prosumers available")
else:
	print("\nComputing Power Reduction Ratios")

	P1RR = P1con/P1gen*PDA
	P1conNew = P1con*P1RR
	P1expNew = P1gen - P1conNew
	P1TariffR = P1exp * btp + (btp * (P1expNew - P1exp) + btp * P1RR * (P1expNew - P1exp))
	P1Tariff = P1expNew * btp

	P1 = {"P1gen":P1gen,"P1exp":P1expNew,"P1con":P1conNew,"P1Tariff":P1Tariff,"P1TariffR":P1TariffR,"P1PDA":P1PDA}
	print(P1)

	P2RR = P2con/P2gen*PDA
	P2conNew = P2con*P2RR
	P2expNew = P2gen - P2conNew
	P2TariffR = P2exp * btp + (btp * (P2expNew - P2exp) + btp * P2RR * (P2expNew - P2exp))
	P2Tariff = P2expNew * btp

	P2 = {"P2gen":P2gen,"P2exp":P2expNew,"P2con":P2conNew,"P2Tariff":P2Tariff,"P2TariffR":P2TariffR,"P2PDA":P2PDA}
	print(P2)

	P3RR = P3con/P3gen*PDA
	P3conNew = P3con*P3RR
	P3expNew = P3gen - P3conNew
	P3TariffR = P3exp * btp + (btp * (P3expNew - P3exp) + btp * P3RR * (P3expNew - P3exp))
	P3Tariff = P3expNew * btp

	P3 = {"P3gen":P3gen,"P3exp":P3expNew,"P3con":P3conNew,"P3Tariff":P3Tariff,"P3TariffR":P3TariffR,"P3PDA":P3PDA}
	print(P3)

	P4RR = P4con/P4gen*PDA
	P4conNew = P4con*P4RR
	P4expNew = P4gen - P4conNew
	P4TariffR = P4exp * btp + (btp * (P4expNew - P4exp) + btp * P4RR * (P4expNew - P4exp))
	P4Tariff = P4expNew * btp

	P4 = {"P4gen":P4gen,"P4exp":P4expNew,"P4con":P4conNew,"P4Tariff":P4Tariff,"P4TariffR":P4TariffR,"P4PDA":P4PDA}
	print(P4)

	P5RR = P5con/P5gen*PDA
	P5conNew = P5con*P5RR
	P5expNew = P5gen - P5conNew
	P5TariffR = P5exp * btp + (btp * (P5expNew - P5exp) + btp * P5RR * (P5expNew - P5exp))
	P5Tariff = P5expNew * btp

	P5 = {"P5gen":P5gen,"P5exp":P5expNew,"P5con":P5conNew,"P5Tariff":P5Tariff,"P5TariffR":P5TariffR,"P5PDA":P5PDA}
	print(P5)

	PANew = P1expNew + P2expNew + P3expNew + P4expNew + P5expNew
	PDANew = PANew/PD
	TotalProsumerCostReward = P1TariffR + P2TariffR + P3TariffR + P4TariffR + P5TariffR
	TotalProsumerCostNoRewardNew = P1Tariff + P2Tariff + P3Tariff + P4Tariff + P5Tariff

	print("Cost Calculations")
	Cost = {"TotalConsumerCost":TotalConsumerCost,"TotalProsumerCostNoReward":TotalProsumerCostNoReward,"TotalProsumerCostNoRewardNew":TotalProsumerCostNoRewardNew,"TotalProsumerCostReward":TotalProsumerCostReward}
	print(Cost)

	print("New Power Balance")
	PB = {"PD":PD,"PA":PA,"PDA":PDA,"PANew":PANew,"PDANew":PDANew}
	print(PB)
