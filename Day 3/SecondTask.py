claims = []
fabric = []
gridSize = 1000

def split_claim(claim):
    claimNo = claim[0]
    x = claim[2].split(",")[0]
    y = claim[2].split(",")[1]
    width = claim[3].split("x")[0]
    height = claim[3].split("x")[1]
    return (int(claimNo), int(x), int(y), int(width), int(height))
    

def apply_claim(claimNo, x, y, width, height):
    for posX in range(x, x + width):
        for posY in range(y, y + height):
            if fabric[posY][posX] == ".":
                fabric[posY][posX] = claimNo
            else:
                fabric[posY][posX] = "X"


def non_overlap(claimNo, x, y, width, height):
    nonOverlap = True  # Assume claim does not overlap
    for posX in range(x, x + width):
        for posY in range(y, y + height):
            if fabric[posY][posX] == claimNo:
                nonOverlap = nonOverlap
            else:
                nonOverlap = False

    if nonOverlap:
        print("The un-overlapped claim is: Claim #{}".format(claimNo))

with open("input.txt", "r") as file_obj:
    for line in file_obj:
        line = "".join([x for x in line if x not in ["#",":","\n"]])
        claims.append(line.split(" "))
        
for i in range(gridSize):
    fabric.append(["." for x in range(gridSize)])

for claim in claims:
    apply_claim(*split_claim(claim)) 
for claim in claims:
    non_overlap(*split_claim(claim))
