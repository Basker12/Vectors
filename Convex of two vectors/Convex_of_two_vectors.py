#Made by Basker12
#Convex of two vectors.

while True:
    v1 = input("Write a vector in the format of x,y: ")
    v1 = v1.split(",")
    v2 = input("Write your second vector in the format of x,y: ")
    v2 = v2.split(",")

    a = float(input("Write a number between 0-1 in the format of 0.00: "))
    if a > 1 or a < 0:
        print("You must write a number between 0-1")
        exit()
    b = float(input("Write another number between 0-1 in the format of 0.00: "))
    if b > 1 or b < 0:
        print("You must write a number between 0-1")
        exit()

    final_v1_1 = int(v1[0])*a
    final_v1_2 = int(v1[1])*a

    final_v2_1 = int(v2[0])*b
    final_v2_2 = int(v2[1])*b

    fin_v1_1 = final_v1_1 + final_v2_1
    fin_v2_2 = final_v1_2 + final_v2_2

    print(fin_v1_1,"," ,fin_v2_2)
