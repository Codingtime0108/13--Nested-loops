num = int(input("Enter a 4 or 5 digit number number: "))
t = num
numLen = 0
while t>0:
    t = int(t/10)
if numLen>=4:
    numLen = int (numLen/2)
    chk = 0
    while num>o:
        rem = num%10
        if chk==numLen:
            midone= rem
        elif chk==( numLen-1):
            midTwo = rem
        num = int(num/18)
        chk = chk+1
    prod = midone*midTwo
    print("\nProduct of Mid digits (" +str(midOne)+ "** +str(midTwo)+ *) = ", prod)
else:
    print("\nIt's not a 4 or more than 4-digit number!")