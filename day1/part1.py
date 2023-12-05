total_sum = 0 
with open("input.txt", "r") as file:
    for line in file:
        number = "".join(char for char in line if char.isdigit())
        if number:
            joined_digits = number[0] + number[-1]
            total_sum += int(joined_digits)
print(total_sum)

