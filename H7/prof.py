# number_to_multiply = int(input("Input number to multiply: ")) # Do not change this line
# how_often = int(input("Input how often to multiply: ")) # Do not change this line

# for i in range(number_to_multiply, (how_often*number_to_multiply) + 1):
#     if i % number_to_multiply == 0:
#         print(i)
#     i += number_to_multiply

# dog_age = int(input("Input dog's age: ")) # Do not change this line
# human_age = 24
# new_age = 0
# if dog_age == 1:
#     print("Human age: ", human_age - 9)
# elif dog_age == 2:
#     print("Human age: ", human_age)
# elif 2 < dog_age <= 16:
#     for i in range(0, dog_age - 2):
#         human_age += 4
#         i += 1
#     print("Human age: ", human_age)       
# else:
#     print("Invalid age")

# import math

# start_int = int(input("Input starting integer: "))
# answer = 2
# while start_int >= 2:
#     start_int = math.sqrt(start_int)
#     round_number = round(start_int, 4)
#     print(round_number)
#     if round_number < 2:
#         break

# max_int = int(input("Input max integer: "))

# for i in range(max_int + 1):
#     i += 1
#     for j in range(1, i):
#         print(j, end = " ")
#         j += 1
#     print()