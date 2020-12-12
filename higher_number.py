#!usr/bin/env python 3
#
# Created by: Dahrio Francois
# Created on: December 2020
# this programs takes two numbers and prints the higher number


def main():
    # this function takes the two numbers and prints the higher number

    # input
    number1 = int(input("Enter your first number: "))
    number2 = int(input("Enter your second number: "))

    # process
    if number1 > number2:
        print("")
        print(number1)
        print(" This number is greater ")

    elif number1 < number2:
        print("")
        print(number2)
        print(" This number is greater ")

    elif number1 == number2:
        print("")
        print(" They are the same number ")


if __name__ == "__main__":
    main()
