s,n=input().split()

def rotate_string(s,d): 
  
    # slice string in two parts for left and right 
    if d==1:
        return(s[-1]+s[:-1])
    else:
        return rotate_string(s[-1]+s[:-1],d-1)


print(rotate_string(s,int(n)))
