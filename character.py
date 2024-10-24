
string = input("Please enter your own word : ")
c = input("Please enter your own Character to search : ")
i = 0
count = 0
while(i < len(string)):
    if(string[i] == c):
        count = count + 1
    i= i + 1
print("The total Number of Times ", c, "has occurred = " ,count)