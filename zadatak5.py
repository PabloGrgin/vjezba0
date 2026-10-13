with open ("intervali.txt" , "r") as file:
    numbers = [line.strip() for line in file if line.strip()]

interval_counts = {}

for num_str in numbers:
    first_digit = num_str[0]
    length = len(num_str)

    interval_key = (first_digit, length)

    if interval_key in interval_counts:
        interval_counts[interval_key] += 1
    else:
        interval_counts[interval_key] = 1

interval_over_100 = 0
for count in interval_counts.values():
    if count > 100:
        interval_over_100 += 1

print(interval_over_100)
