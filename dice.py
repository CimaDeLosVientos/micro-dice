from microbit import *

import random

dice = ["d4", "d6", "d8", "d10", "d12", "d20", "d100"]

diceSelect = 0

diceChange = 0

maxDice = {
	0:4,
	1:6,
	2:8,
	3:10,
	4:12,
	5:20,
	6:100
}

def change_dice(next):
	diceSelect = (diceSelect + next) % len(dice)
	display.scroll(str(dice[diceSelect]))

	
while True:

	if (button_a.was_pressed()):
		change_dice(1)

	if (button_b.was_pressed()):
		change_dice(-1)

	if (accelerometer.was_gesture('shake')):
		maxNumber = maxDice[diceSelect]
		number = random.randint(1, maxNumber)
		display.scroll(str(number))
