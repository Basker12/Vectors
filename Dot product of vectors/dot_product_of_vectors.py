#Made by Basker12
#Dot product of a vector.

v1 = input("Write your vector in the format of x,y: ")
v1 = v1.split(",")
v2 = input("Write your second vector in the format of x,y: ")
v2 = v2.split(",")

final_v1 = int(v1[0])*int(v2[0])
final_v2 = int(v1[1])*int(v2[1])


dot_product = final_v1 + final_v2
print(dot_product)
