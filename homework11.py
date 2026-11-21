# loop art designer

# part 1: star pyramid pattern
print("===== star pyramid pattern =====")

rows = int(input("enter number of rows for star pattern: "))

for i in range(rows):
    for j in range(i + 1):
        print("* ", end="")
    print()


# part 2: floyd's triangle pattern
print("
===== floyd's triangle =====")

rows = int(input("enter number of rows for floyd's triangle: "))
number = 1

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(number, end=" ")
        number += 1
    print()


# part 3: diamond number pattern
print("
===== diamond number pattern =====")

row_size = int(input("enter number of rows for diamond pattern: "))

if row_size % 2 == 0:
    half_rows = row_size // 2
else:
    half_rows = row_size // 2 + 1

space = half_rows - 1

# upper half of diamond
for i in range(1, half_rows + 1):
    for j in range(1, space + 1):
        print(" ", end="")

    space -= 1
    number = 1

    for j in range(2 * i - 1):
        print(number, end="")
        number += 1

    print()

# lower half of diamond
space = 1

for i in range(1, half_rows):
    for j in range(1, space + 1):
        print(" ", end="")

    space += 1
    number = 1

    for j in range(1, 2 * (half_rows - i)):
        print(number, end="")
        number += 1

    print()


# part 4: final message
print("
===== loop art design complete =====")
print("you created star, triangle, and diamond patterns using nested loops!")