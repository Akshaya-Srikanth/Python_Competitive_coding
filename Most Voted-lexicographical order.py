In a school there are voting to choose the monitor of class.
Your task is to tell which candidate is winner and if there is a tie print the name of candidate whose come first in lexicographical order.

Input Description:
You are given with the space separated names.

Output Description:
Print the winner’s name and the votes he earned.

Sample Input :
john johnny jackie johnny john jackie jamie jamie john johnny jamie johnny john

CODE:

s=input().split()
s1=set(s)
d=dict.fromkeys(sorted(s1))

for x in s1:
    d[x]=s.count(x)
    
k=list(d.keys())
v= list(d.values())
max_v=max(d.values())
print( k[v.index(max_v)],max_v)
