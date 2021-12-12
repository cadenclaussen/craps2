import random
amount_won = 0
amount_lost = 0
total_bet = 0
for i in range(10000000):
	number1 = random.randint(1, 6) + random.randint(1, 6)
	original_bet = 10
	total_bet += original_bet
	# Phase 1
	if number1 == 2 or number1 == 3 or number1 == 12:
		amount_lost += original_bet
		continue
	if number1 == 7 or number1 == 11:
		amount_won += original_bet
		continue

	# Phase 2
	newbet = original_bet * 2
	total_bet += newbet
	p2dict = {"2":1, "3":2, "4":3, "5":4, "6":5, "7":6, "8":5, "9":4, "10":3, "11":2, "12":1}
	point = number1
	number2 = random.randint(1, 6) + random.randint(1, 6)
	while number2 != point and number2 != 7:
		number2 = random.randint(1, 6) + random.randint(1, 6)
	if number2 == 7:
		amount_lost = amount_lost + (newbet + original_bet)
	else:
		amount_won = amount_won + original_bet + newbet * int(p2dict["7"])/int(p2dict[str(point)])

print("Amount Won: " + str(amount_won))
print("Amount Lost: " + str(amount_lost))
print("Total Bet: " + str(total_bet))
delta = amount_lost - amount_won
print("Delta: " + str(delta))
print("Percent Lost: " + str(delta/total_bet * 100) + "%")