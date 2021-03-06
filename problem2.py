def testLeap(num):
    if ((yearInput) % 4) == 0:
        if ((yearInput) % 100) == 0:
            if ((yearInput) % 400) == 0:
                print("The entered year is a leap year")
            else:
                print("The entered year is not a leap year")
        else:
            print("The entered year is a leap year")
    else:
        print("The entered year is not a leap year")