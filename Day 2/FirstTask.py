IDs = []
twoCount = 0
threeCount = 0

with open("input.txt", "r") as file_obj:
    IDs = [line.strip() for line in file_obj]

    for ID in IDs:
        two = False
        three = False
        ID = list(ID)
        IDCount = set([(i, ID.count(i)) for i in ID])
        
        for count in IDCount:
            if count[1] == 2 and not two:
                twoCount += 1
                two = True
            if count[1] == 3 and not three:
                threeCount += 1
                three = True

    print(twoCount * threeCount)
