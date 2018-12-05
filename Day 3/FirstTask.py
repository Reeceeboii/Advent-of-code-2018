claims = []
fabric = []

def apply_claim(claimNo, x, y, width, height):
    print("Claim {} @ {},{} -- {}x{}".format(claimNo, x, y, width, height))

    for i in range (width):
        for j in range (height):
            print(claimNo, end = "")
        print()

    for i in range(x):
        for j in range(y):
            claims[x:width][y:height] = claimNo
    

with open("test.txt", "r") as file_obj:
    for line in file_obj:
        line = "".join([x for x in line if x not in ["#",":","\n"]])
        claims.append(line.split(" "))
        
for i in range(8):
    fabric.append(["." for x in range(8)])

for claim in claims:
    claimNo = claim[0]
    x = claim[2].split(",")[0]
    y = claim[2].split(",")[1]
    width = claim[3].split("x")[0]
    height = claim[3].split("x")[1]
    apply_claim(int(claimNo), int(x), int(y), int(width), int(height))

    for x in fabric:
        for y in x:
            print(y, end = "")
        print()
