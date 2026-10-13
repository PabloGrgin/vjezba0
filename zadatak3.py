with open ("kocka.txt", "r") as file:
    lines = [line.strip() for line in file if line.strip()]
counter = 0
for line in lines:
    sequences = line.split(",")
    yes = False

    for seq in sequences:
        numbers_count = [0,0,0,0,0,0]

        for char in seq:
            number = int(char)
            numbers_count[number-1] += 1
        
        add = True
        for i in range(5):
            if numbers_count[5] <= numbers_count[i]:
                add = False
                break

        if add == True:
            yes = True
            break

    if yes == True:
        counter += 1

print({counter})