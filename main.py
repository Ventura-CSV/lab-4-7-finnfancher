def main():
    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """
    index = 0
    numbers.append(int(input("enter a number: ")))
    while(True):
        num1 = (int(input("enter a number: ")))
        if(num1 > numbers[index]):
            break
        numbers.append(num1)
        index += 1

    ########################################
    # Do not delete the return statement
    ########################################
    print(numbers)
    return numbers


if __name__ == '__main__':
    main()
