claims = []
fabric = []
gridSize = 1000
count = 0

def apply_claim(claimNo, x, y, width, height):
    for posX in range(x, x + width):
        for posY in range(y, y + height):
            if fabric[posY][posX] == ".":
                fabric[posY][posX] = claimNo
            else:
                fabric[posY][posX] = "X"
                
            
with open("input.txt", "r") as file_obj:
    for line in file_obj:
        line = "".join([x for x in line if x not in ["#",":","\n"]])
        claims.append(line.split(" "))
        
for i in range(gridSize):
    fabric.append(["." for x in range(gridSize)])

for claim in claims:
    claimNo = claim[0]
    x = claim[2].split(",")[0]
    y = claim[2].split(",")[1]
    width = claim[3].split("x")[0]
    height = claim[3].split("x")[1]
    apply_claim(int(claimNo), int(x), int(y), int(width), int(height))

for squareInch in fabric:
    for claim in squareInch:
        if claim == "X":
            count += 1

print("The number of square inches within 2 or more claims is: {}".format(count))







