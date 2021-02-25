#Made by Basker12

#Multiplying vectors.

v1 = input("Write your vector in the format of x,y: ")
v1 = v1.split(",")
v2 = input("Write your second vector in the format of x,y: ")
v2 = v2.split(",")

final_v1 = int(v1[0])*int(v2[0])
final_v2 = int(v1[1])*int(v2[1])

print(final_v1, "," , final_v2)

#Multiplying vectors using scalars.

v3 = input("Write your vector in the format of x,y: ")
v3 = v3.split(",")
v4 = input("Write your second vector in the format of x,y: ")
v4 = v4.split(",")

s_num = int(input("Write a scalar number: "))

final_v3 = int(v3[0]) * s_num + int(v3[1]) * s_num
final_v4 = int(v4[0]) * s_num + int(v4[1]) * s_num

s_multi = final_v3 + final_v4
print(s_multi)
