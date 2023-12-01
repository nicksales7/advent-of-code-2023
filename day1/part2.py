def words_to_numbers(s):
    number_words = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10
    }

    while True:
        found_word = False
        for i in range(len(s)):
            for j in range(i+1, len(s) + 1):
                substring = s[i:j]
                if substring in number_words:
                    number = number_words[substring]
                    replacement = f"{number}{substring[-1]}"
                    s = s[:i] + replacement + s[j:]
                    found_word = True
                    break 
            if found_word:
                break  

        if not found_word: 
            break

    return s


total_sum = 0 
with open("puzzle-input.txt", "r") as file:
    for line in file:
        new_string = words_to_numbers(line)
        number = "".join(char for char in new_string if char.isdigit())
        if number:
            joined_digits = int(number[0] + number[-1])
            total_sum += joined_digits

print(total_sum)