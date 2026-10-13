import itertools

with open ("brojevi.txt", "r") as file:
    lines = [line.strip() for line in file if line.strip()]

overall_max = 0

for line in lines:
    numbers = [num for num in line.split(';') if num]

    for perm in itertools.permutations(numbers):
        combined_number = int(''.join(perm))

        if combined_number > overall_max:
            overall_max = combined_number

print(overall_max)