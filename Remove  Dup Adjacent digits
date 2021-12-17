Question:
You are given a number with duplicate digits your task is to remove the immediate duplicate digits and print the result

Input Description:
You are given a long string of digits

Output Description:
Print the desired result print -1 if result length is 0

Sample Input :
1331
Sample Output :
11


Code:


def remove_adjacent(nums):
    temp_list = []

    for item in nums:   
        if len(temp_list) == 0:
            temp_list.append(item)

        elif len(temp_list) > 0:
            if  item != temp_list[-1]:
                temp_list.append(item)
            else:
                temp_list[temp_list.index(item)]= "*"
    if "*" in temp_list:
        temp_list.remove("*")
    return(''.join(temp_list))
     
  
s=input()
a=remove_adjacent(s) 
if(len(a)== 0):
    print('-1')
else:
    print(a)
