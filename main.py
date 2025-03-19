import unittest


def Add(numbers):
    if numbers == "":
        return 0
    numbers=numbers.replace("\n", ",")
    if ",," in numbers:
        return "!"

    numbersToAdd=numbers.split(",")
    sum=0
    for num in numbersToAdd:
        sum=sum+int(num)
    return sum


if __name__ == "__main__":
    unittest.main()





