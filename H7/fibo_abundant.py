start = str(input("Input f|a|b (fibonacci, abundant or both): "))


if start == "f":
    length = int(input("Input the length of the sequence: "))
    print("Fibonacci Sequence:")
    print("-------------------")
    number_1 = 0
    number_2 = 1
    number_total = 0
    for n in range(length):

        print(number_1)

        number_total = number_1 + number_2

        number_1 = number_2

        number_2 = number_total

        n += 1

elif start == "a":
    max = int(input("Input the max number to check: "))
    print("Abundant numbers:")
    print("-----------------")
    abundant = 0
    
    for i in range(max+1):

        for j in range(1, i):

            if i % j == 0:

                abundant += j
        
        if abundant > i:

            print(i)

        abundant = 0

elif start == "b":

    length = int(input("Input the length of the sequence: "))
    print("Fibonacci Sequence:")
    print("-------------------")
    number_1 = 0
    number_2 = 1
    number_total = 0
    for n in range(length):
        print(number_1)

        number_total = number_1 + number_2

        number_1 = number_2

        number_2 = number_total

        n += 1

# second part
    max = int(input("Input the max number to check: "))
    print("Abundant numbers:")
    print("-----------------")
    abundant = 0
    
    for i in range(max+1):

        for j in range(1, i):

            if i % j == 0:

                abundant += j
        
        if abundant > i:

            print(i)

        abundant = 0
