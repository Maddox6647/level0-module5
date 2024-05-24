"""
Write code that can tell if a number is prime.
A prime number is a number that is only divisible by 1 and itself.
"""
import random
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    # TODO)
    #  1. Ask the user for a number
    #  2. Use a for loop, if statement, and modulo to find if the number
    #     is prime.
    #  3. If the number is divisible by any number other than 1 or itself,
    #     the number is not prime.
    window = Tk()
    window.withdraw()

    bobby = simpledialog.askinteger(title='hi', prompt='enter a number greater than 1')
    if bobby < 2:
        exit()
    for i in range(2, bobby):
        if bobby % i == 0:
            print('not prime mister no brain')

