# Program to divide two numbers without using the division operator
def divide(ourdividend, ourdivisor):
    # Check if divisor is positive or negative
    sign = (-1 if(ourdividend<0) ^ (ourdivisor<0) else 1);
# Make both positive 
    ourdividend = abs(ourdividend);
    ourdivisor = abs(ourdivisor);
    quotientnumber = 0
    tempnumber = 0
# Go from 31 to 0 and accumilate all valid bits
    for i in range(31, -1, -1):
        if (tempnumber + (ourdivisor<<i) <= ourdividend):
            tempnumber += ourdivisor<< i
            quotientnumber |= 1<<i
# Assuming the sign value computed earlier is -1, negate the quotient value
    if sign == -1:
        quotientnumber = -quotientnumber
    return quotientnumber
a = int(input("Enter a for a/b:"))
b = int(input("Enter b for a/b:"))
print("result of", a,"/", b,"is:",divide(a,b))