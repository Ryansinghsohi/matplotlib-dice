import matplotlib.pyplot as plt
import random

amount_of_rolls = 10
dice_results = [0]


def mean_value():
    sum_of_dice = 0
    for N in range(0, amount_of_rolls, 1):
        dice_value = dice_results[N]
        sum_of_dice += dice_value
        N += 1
    mean = sum_of_dice/amount_of_rolls
    return print(f'The mean is: {mean}')


for i in range(0, amount_of_rolls, 1):
    dice_roll = random.randint(1, 6)
    dice_results.append(dice_roll)
    i += 1

mean_value()
plt.plot(dice_results, "b-", dice_results, "bo")
plt.axis((1, amount_of_rolls, 0, 6))
plt.ylabel("dice value")
plt.xlabel("dice roll")
plt.title("dice roll probability")
plt.show()
