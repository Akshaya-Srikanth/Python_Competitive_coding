Given a string S, print the encoded string by adding 3 to each character(a maps to d,b maps to e,c maps to f and so on).
Input Size : 1 <= N <= 100000
Sample Testcase :
INPUT
RADAR
OUTPUT
UDGDU









CODE:
def decode(s):
    s1=""
    for x in s:
        if ord(x) in range(97,123):
            s1 +=chr(((ord(x)+3-96)%26)+96)
        elif ord(x) in range(65,90):
            s1 +=chr((ord(x) + 3 - 64)%26+64)

    print(s1)
        
s=input()
decode(s)
#print(ord('a'),ord('z'))
