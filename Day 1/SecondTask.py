currentFreq = 0
freqChanges = []
previousFreqs = set()
found = False

with open("input.txt","r") as file_obj:
    freqChanges = [int(line.strip()) for line in file_obj]

while not found:
    for change in freqChanges:
        currentFreq += change

        if currentFreq in previousFreqs:
            print(currentFreq)
            raise SystemExit

        previousFreqs.add(currentFreq)

