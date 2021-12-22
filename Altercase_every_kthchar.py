Given a string and a number K, change every kth character to uppercase from beginning in string.
Sample Testcase :
INPUT
string 2
OUTPUT
sTrInG

Input:
string 0
Expected Output:
string

CODE:
def altercase(Arr,K):
    arr1=[]
    for x in Arr:
        arr1.append(x)
    #print(arr1)
    if K>0:
        for k in range(K-1,len(arr1),K):
            arr1[k]=Arr[k].upper()
    return arr1



Arr,K=input().split()

print(*altercase(Arr,int(K)),sep="")
