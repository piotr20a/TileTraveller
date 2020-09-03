# n = int(input("Input a natural number: ")) # Do not change this line

# # Fill in the missing code below
# while n >= 1:
#     if n == 1:
#         print("Not prime")
#         break
#     elif n % 2 != 0 or n == 2:
#         print("Prime")
#         break
#     else:
#         print("Not prime")
#         break

# i = 10
# result = None
# while i < 100:
#     if str(i ** i)[-2::] == str(i):
#         result = i
#     i += 1
# print(result)

# i = 10
# result = None
# while i < 100:
#     number = i ** 2
#     if str(i**2)[-2::] == str(i):
#         result = i
#     i += 1
# print(result)

# i = 10
# while i < 100:
#     c = 1w
#     while c < 10:
#         if (i*i) == (i+100*c):
#             print(i)
#         c += 1
#     i += 1

# import math

# # These lines you can keep as is
# print("Think of a number between 1 and 100 (inclusive)")
# print("I am going to guess what it is")
# input("Press enter when you are ready to play")

# # Here you might want to initialize some variables

# guess = 50
# min_num = 1
# max_num = 100
# i = 0

# # Then start a while loop
# while i <= 7:
#     guess = int((min_num + max_num) / 2)
#     # These lines you can keep as is
#     print("Is the number", guess, "?")
#     print("Type one of the following letters and press enter:")
#     print("h: if the guess is too (h)igh")
#     print("l: if the guess is too (l)ow")
#     print("c: if the guess is (c)orrect")
#     print("q: to (q)uit the game")
#     cmd = input() 

#     # Now it's up to you to check the command and take appropriate action
#     if cmd == "q":
#         print("Quitter")
#         break
#     elif cmd == "c":
#         print("I AM VICTORIOUS")
#         break
#     elif cmd == "h":
#         num_max = guess - 1
#         guess = math.floor((min_num + num_max) / 2)
#     elif cmd == "l":

#         num_max = guess + 1
#         guess = math.floor((min_num + num_max) / 2)
    
#     i += 1


# # If you detect that the user has not been truthful, you should print the following
# print("Tsk, tsk, don't try to cheat me")


# print("Think of a number between 1 and 100 (inclusive)")
# print("I am going to guess what it is")
# input("Press enter when you are ready to play")

# i = 0
# num_min = 1
# num_max = 100
# guess = 50
# cmd = None
# while True:
#     i += 1
#     if i > 7:
#         print("Tsk, tsk, don't try to cheat me")
#         break
#     guess = int((num_min + num_max) / 2)

#     print("Is the number", guess, "?")
#     print("Type one of the following letters and press enter:")
#     print("h: if the guess is too (h)igh")
#     print("l: if the guess is too (l)ow")
#     print("c: if the guess is (c)orrect")
#     print("q: to (q)uit the game")
#     cmd = input()

#     if cmd == "h":
#         num_max = guess - 1
#     elif cmd == "l":
#         num_min = guess + 1
#     elif cmd == "c":
#         print("I AM VICTORIOUS") 
#         break
#     elif cmd == "q": 
#         print("Quitter") 
#         break


# upto = int(input("Input an int: "))  # Do not change this line

# for i in range(1, upto):
#     print(i)

# highest = int(input("Input an int: "))

# for i in range(1, highest+1):
#     if i % 3 == 0:
#         print(i)

# first = int(input("Input the first integer: "))
# second = int(input("Input the second integer: "))

# sum = 0

# for i in range(first):
#     sum += second
# print(sum)

# max_days = int(input("Input max number of days: "))
# target = int(input("Input dollar target: "))
# dollar = 0
# days_when_amount_acquired = 0
# # Fill in the missing code
# for i in range(max_days):

#     dollar = (dollar + pow(2, i))
#     if dollar >= target:
#         days_when_amount_acquired = i + 1
#         break
#     else:
#         days_when_amount_acquired = 0

# print('Days needed:',days_when_amount_acquired)

# summa = 0
# num = int(input("Input an int: ")) # Do not change this line
# for i in range(1, num + 1):
#     sum = 0
#     for n in range(1, i + 1):
#          sum += j
#     print(sum)

# max_num = int(input("Input maximum number: "))

# for i in range(1, max_num + 1):
#     summa = 0
#     for n in str(i):
#         summa += int(ch)
#     if summa ** 3 == i:
#         print(i)

# Don't change the following lines
# import math

# number_of_cycles = float(input("Number of cycles: "))
# number_of_lines = int(input("Stretched over how many lines? "))

# radians_per_line = number_of_cycles * 2 * math.pi / number_of_lines

# for i in range(number_of_lines):
#     radians = i * radians_per_line
#     sine_value = round(math.sin(radians) * 20 + 20)
#     print("X"*sine_value)

# Read exactly four lines of input
line1 = input()
line2 = input()
line3 = input()
line4 = input()

# Define variables for the range of numbers within which we have 'printable' characters.
# As we shift the input characters, we must ensure that they stay within this range.
LOW = ord(" ")  # 32
HIGH = ord("~") # 126
RANGE = HIGH - LOW
# Every transmission starts with the line "Hail Caesar!" so the first letter, 
# once decrypted, must be H.
first_letter = line1[0]
key = 0
for i in range(RANGE + 1):
    if ord(first_letter) == HIGH:
        first_letter = chr(LOW)
    else:
        first_letter = chr(ord(first_letter) + 1)
    key += 1

    if first_letter == "H":
        break

# ...now find out what the key is
# We can use 'for' to iterate over the lines and decrypt them one by one
for line in (line1, line2, line3, line4):
    # ... and the rest is up to you
    new_line = ''
    for char in line:
        new_letter = char
        for i in range(key):
            if ord(new_letter) == HIGH:
                new_letter = chr(LOW)
            
            else:

                new_letter = chr(ord(new_letter) + 1)
            new_line += new_letter
        
        print(new_line)
