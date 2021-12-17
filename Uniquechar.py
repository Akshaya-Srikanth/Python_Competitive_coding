You are given a string ‘S’ consisting of lowercase Latin Letters. Find the first non repeating character in S. If you find all the characters are repeating print the answer as -1

Input Description:
You are given a string ‘s’

Output Description:
Print the first non occurring character if possible else -1.

Sample Input :
apple
Sample Output :
a

Code:
def nondup(string):
    l=[]
    for x in string:
        if x not in l and string.count(x) ==1 :
            l.append(x)

    return l
    
s=input()
a=nondup(s)
print( '-1' if len(a)==0 else a[0])

        


