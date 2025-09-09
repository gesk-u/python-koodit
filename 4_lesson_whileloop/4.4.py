import random

dice1 = dice2 = rolls = 0

while dice1 != 6 and dice2 != 6:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    rolls += 1



total_r = rolls
av_r = total_r/rounds
