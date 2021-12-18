You are given two strings . Your task is to tell whether the pair of strings is panagram.
A pair of strings are said to be panagram if they both are palindrome and are anagram of each other.

Input Description:
You will be given two strings ‘s1’ and ‘s2’

Output Description:
Print 1 if they are panagram and 0 if they are not

Sample Input :
nitin intni
Sample Output :
1

Code:
def palindrome(s1,s2):
    if s1[::] == s1[::-1] and s2[::] == s2[::-1]:
        return True
    return False
    
def anagram(s1,s2):
    if sorted(s1) == sorted(s2):
        return True
    return False

s1,s2=input().split()

if palindrome(s1,s2) == True and anagram(s1,s2) ==True:
    print('1')
else:
    print('0')
      
  
  
