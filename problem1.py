def FizzBizz():
    string = ""
    for i in range(1, 100):

        if i % 3 == 0:
            string = string + "Fizz"

        if i % 5 == 0:
            string = string + "Buzz"
        if (i % 5 != 0) and (i % 3 != 0):
            string = string + str(i)
    print(string)
    return string



FizzBizz()
