__author__ = 'Kellan Childers'
from random import randint


def roll(count, dice_sides):
    return sum([randint(1, dice_sides) for _ in range(count)])


def fate_roll():
    return sum([randint(-1, 1) for _ in range(5)])

if __name__ == "__main__":
    print("Rolling 2d6: " + str(roll(2, 6)))
    print("Rolling 4dF: " + str(fate_roll()))
