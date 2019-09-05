from math import floor
def large_multiply(x,y):
    str_x = str(x)
    str_y = str(y)
    if len(str_x)==1 or len(str_y)==1:
        return x*y
    else:
        n = max(len(str_x),len(str_y))
        nby2 = floor(n / 2)
        
        a = int(x / 10**(nby2))
        b = x % 10**(nby2)
        c = int(y / 10**(nby2))
        d = y % 10**(nby2)
        
        ac = large_multiply(a,c)
        bd = large_multiply(b,d)
        ad_plus_bc = large_multiply(a+b,c+d) - ac - bd
        
            # this little trick, writing n as 2*nby2 takes care of both even and odd n
        prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd

        return prod

def main():
    lines = ""
    with open("inputPS2.txt", encoding='utf8') as fin:
        lines = fin.read().strip()
    splitLines = lines.split("\n")
    num1 = splitLines[0]
    num2 = splitLines[1]
    ans=large_multiply(int(num1), int(num2))
    print(ans)
    
if __name__== "__main__":
    main()
