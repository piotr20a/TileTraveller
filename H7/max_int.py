lista = []
max_int = 0
while True:
    num_int = int(input("Input a number: "))
    if num_int < 0:
        break
    lista.append(num_int)

max_int = max(lista)

print("The maximum is", max_int)    # Do not change this line
