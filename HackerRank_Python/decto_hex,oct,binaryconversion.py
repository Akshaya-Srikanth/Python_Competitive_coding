def print_formatted(number):
    # your code goes here
    lst = []
    width=len(bin(number)[2:])
    #print(width)
    for i in range(1, n + 1):
        print( str(i).rjust(width,' '),str(oct(i)).replace("0o","").rjust(width,' '),str(hex(i)).replace("0x","").upper().rjust(width,' '),str(bin(i)).replace("0b","").rjust(width,' '))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
