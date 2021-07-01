#exercise_1
#Basic Program
a = int(input("please Enter count of Students: "))
avr1,avr2 = 0,0
id2 , id1 = 0,0
for val in range (1,a+1):
    id = int(input("Please Enter Student ID: "))
    avr = int(input("please Enter Mark:"))
    if avr > avr1 :
        avr2 = avr1
        id2 = id1
        id1 = id
        avr1 = avr
    elif avr > avr2 :
        avr2 = avr
        id2 = id

else:
    print(f"{id2} : {avr2}")
