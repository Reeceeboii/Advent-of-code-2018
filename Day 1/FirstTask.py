freq = 0

with open("input.txt", "r") as file_obj:
    for line in file_obj:
        if line[0] == "+":
            freq += int(line.strip("+"))
        else:
            freq -= int(line.strip("-"))

    print("Frequency: {}".format(freq))