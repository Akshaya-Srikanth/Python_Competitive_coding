'''
x,y = map(int,input().split())
pattern= [(".|."*((2*i)+1)).center(y,"-")  for i in range(x//2)]
#print(pattern)
print('\n'.join(pattern+["WELCOME".center(y,"-")]+ pattern[::-1]))
'''
'''
#print (".|.".ljust(20,"-"))



print(	"\n".join([str(x**2)  for x in range(5)]))
num=[x**2  for x in range(5)]
print(*num,sep="\n")
'''
'''
x = int(input())
pattern= [(chr(91+i)*((2*i)+1)).center(y,"-")  for i in range(x//2)]
#print(pattern)
print('\n'.join(pattern+["WELCOME".center(y,"-")]+ pattern[::-1]))
'''

import string
st=string.ascii_lowercase
n = int(input())
lst=[]
for i in range(n):
    alpha="-".join(st[i:n])
    lst.append((alpha[::-1]+ alpha[1:]).center(4*n+3,'-'))
print("\n".join(lst[::-1]+lst[1:]))

