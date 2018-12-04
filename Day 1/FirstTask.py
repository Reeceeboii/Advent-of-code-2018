freq = 0

with open("input.txt", "r") as file_obj:
    for line in file_obj:
        freq += int(line.strip())

    print("Frequency: {}".format(freq))
