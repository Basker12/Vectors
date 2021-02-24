#Made by Basker12
#Adding and subtracting two vectors.

#Adding
while True:
    v1 = input("Write a vector in the format of x,y: ")
    v1 = v1.split(",")
    v2 = input("Write a second vector in the format of x,y: ")
    v2 = v2.split(",")

    final_v1 = int(v1[0])+int(v2[0])
    final_v2 = int(v1[1])+int(v2[1])

    print(final_v1, "," , final_v2)

    #Subtracting

    v3 = input("Write a vector in the format of x,y: ")
    v3 = v3.split(",")
    v4 = input("Write a vector in the format of x,y: ")
    v4 = v4.split(",")

    final_v3 = int(v3[0])-int(v4[0])
    final_v4 = int(v3[1])-int(v4[1])

    print(final_v3, "," , final_v4)
