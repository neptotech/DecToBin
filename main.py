# from Graph import grplt as grp
# grp([1,3,5,7],[2,4,6,1])

# print(bin(253101864345684230562631562564982518153418969132))
import time
from math import trunc

begin = time.perf_counter()

decimal = 253101864345684230562631562564982518153418969132
binary = ""
binaryHolder = 1
temp = 1

while 158 >= temp:
    Algorithm = (decimal // binaryHolder) % 2
    binary = str(trunc(Algorithm)) + binary
    binaryHolder += binaryHolder
    temp += 1

print(binary)
end = time.perf_counter()

print(f"Total runtime of the program is {end - begin}")


begin = time.perf_counter()

#get input and initialize variables
decimal = 253101864345684230562631562564982518153418969132
binary = 0
ctr = 0
temp = decimal  #copy input decimal

#find binary value using while loop
while(temp > 0):
    binary = ((temp%2)*(10**ctr)) + binary
    temp = int(temp/2)
    ctr += 1

#output the result
print(binary)

end = time.perf_counter()

print(f"Total runtime of the program is {end - begin}")
print(bin(253101864345684230562631562564982518153418969132))