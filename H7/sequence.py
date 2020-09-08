number_1 = 1
number_2 = 2
number_3 = 3
sum_number = 0
num = 0
n = int(input("Enter the length of the sequence: "))
print(number_1)
print(number_2)
print(number_3)
for i in range(n-3):
    sum_number = number_1 + number_2 + number_3
    number_1 = number_2
    number_2 = number_3
    number_3 = sum_number
    print(sum_number)
