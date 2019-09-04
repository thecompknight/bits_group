from math import floor
def karatsuba(x,y):
    """Function to multiply 2 numbers in a more efficient manner than the grade school algorithm"""
    str_x = str(x)
    str_y = str(y)
    if x<10 or y<10:
        return x*y
    else:
        n = max(len(str_x),len(str_y))
        nby2 = floor(n / 2)
        
        a = int(x / 10**(nby2))
        b = x % 10**(nby2)
        c = int(y / 10**(nby2))
        d = y % 10**(nby2)
        
        ac = karatsuba(a,c)
        bd = karatsuba(b,d)
        ad_plus_bc = karatsuba(a+b,c+d) - ac - bd
        
            # this little trick, writing n as 2*nby2 takes care of both even and odd n
        prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd

        return prod

def main():
    ans=karatsuba(int(2554), int(4535))
    print(ans)
    
if __name__== "__main__":
    main()
