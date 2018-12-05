IDs = []

with open("input.txt", "r") as file_obj:
    IDs = [list(line.strip()) for line in file_obj]


for ID in IDs:
    for IDComparator in IDs:
        if ID != IDComparator: # compares every ID to every other ID bar itself
            difference = 0
            differenceLocation = 0
            for i in range (0, (len(ID))):
                if ID[i] != IDComparator[i]:
                    difference += 1
                    differenceLocation = i

            if difference == 1:
                del ID[differenceLocation]
                print("".join([x for x in ID]))
                raise SystemExit
            
                
                
