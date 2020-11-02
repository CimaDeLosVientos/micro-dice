from microbit import *

import random

dice = ["d4", "d6", "d8", "d10", "d12", "d20", "d100"]

diceSelect = 0

diceChange = 0

maxDice = {0:4,1:6,2:8,3:10,4:12,5:20,6:100}

while True:

	if (button_a.was_pressed()):
		diceChange = 1
		diceSelect += 1
		if (diceSelect >= 7):
			diceSelect = 0


	if (button_b.was_pressed()):
		diceChange = 1
		diceSelect -= 1
		if (diceSelect < 0):
			diceSelect = 6


	if (diceChange):
		diceChange = 0
		display.scroll(str(dice[diceSelect]))


	if (accelerometer.was_gesture('shake')):
		maxNumber = maxDice[diceSelect]
		number = random.randint(1, maxNumber)
		display.scroll(str(number))
