freq = 0

with open("input.txt", "r") as file_obj:
    for line in file_obj:
        if line[0] == "+":
            print(line)
            freq += int(line.strip("+"))
        else:
            print(line)
            freq -= int(line.strip("-"))

    print("Frequency: {}".format(freq))
