def testLeap(num):
    if num % 4 == 0:
        if ((yearInput) % 100) == 0:
            return "The entered year is a leap year"
        else:
            return "The entered year is not a leap year"
    else:
        return"The entered year is not a leap year"
