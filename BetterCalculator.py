prompt_loop = True
continous_prompt = True


def calculation():
    global digitOne, digitTwo, result
    while prompt_loop:
        try:
            digitOne = float(input("Enter first number: "))

            while not "+" or "-" or "/" or "*":
                operator = input("Enter operator: ")
                if operator == "+" or operator == "-" or operator == "/" or operator == "*":
                    break
                else:
                    print("Wrong chracter try again")
                    continue

            digitTwo = float(input("Enter Second number: "))
        except ValueError:
            print("Wrong chracter try again")
            continue
        if operator == "+":
            result = digitOne + digitTwo
            print(result)
            break;

        elif operator == "-":
            result = digitOne - digitTwo
            print(result)
            break;

        elif operator == "*":
            result = digitOne * digitTwo
            print(result)
            break;

        elif operator == "*":
            result = digitOne * digitTwo
            print(result)
            break;

        elif operator == "/":
            if operator == "/" and digitOne == 0 and digitTwo > 0:
                print("You can't divide by 0")
                continue;
            elif operator == "/" and digitTwo == 0 and digitOne > 0:
                print("You can't divide by 0")
                continue;
            else:
                result = digitOne // digitTwo
                print(result)
                break;

    while continous_prompt:
        try:
            while not "+" or "-" or "/" or "*":
                operator = input("Enter operator: ")
                if operator == "+" or operator == "-" or operator == "/" or operator == "*":
                    break
                else:
                    print("Wrong chracter try again")
                    continue
            extra_number = float(input("Enter a number: "))

        except ValueError:
            print("Wrong chracter try again")
        if operator == "+":
            result += extra_number
            print(result)
        elif operator == "-":
            result -= extra_number
            print(result)
        elif operator == "*":
            result *= extra_number
            print(result)
        elif operator == "/":
            if operator == "/" and digitOne == 0 and digitTwo > 0:
                print("You can't divide by 0")
                continue;
            elif operator == "/" and digitTwo == 0 and digitOne > 0:
                print("You can't divide by 0")
                continue;
            else:
                result /= extra_number
            print(result)
            break;
        erase_or_not = input("do you want to continue or erase results? Y/N")
        if erase_or_not == "Y" or erase_or_not == "y":
            result = 0
            calculation()


calculation()
