import random
#Receive number of dice
dice = int(input("How many dice to roll? "))


sum_dice = 0
#iterate 'dice' times 
for i in range(dice):
    result = random.randint(1, 6)
    sum_dice += result

# Print the result
print(f"Sum of dice: {sum_dice}")

