def symbol_index(lst):
    not_symbols = set("0123456789.")
    return [[i, j] for i, row in enumerate(lst) for j, char in enumerate(row) if char not in not_symbols]

with open("input.txt", "r") as file:
    data = file.read().splitlines()
    print(symbol_index(data))
