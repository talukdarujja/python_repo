import math
radius=5
def circum(r):
    circum=math.pi*r*2
    return circum

print(circum(radius))

# total=0
# for i in range(1,6):
#     total+=i
#     print(total)

    # for fruits in ["apple","kiwi"]:
    # print(fruits)
# stars=0
# for i in range(1,8):
#     for i in range(1,8):
#         stars+=i
#         print("*")

rows = 7
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, i + 1):  # Inner loop for columns
        print("*", end=" ")   # Print star
    print()
    