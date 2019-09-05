from math import floor

def large_multiply(str_x,str_y, f):
    
    #check for single digit
    if len(str_x)==1 or len(str_y)==1:
        return str(int(str_x)*int(str_y))
    else:
        
        #Identify the number of digits involved
        n = max(len(str_x),len(str_y))
        nby2 = floor(n / 2)
        
        #use multiplication by 10 to bring numbers to same length if they are not already
        x_padding = n-len(str_x)
        y_padding = n-len(str_y)
        
        str_x = pad_with_zeros_to_right(str_x, n)
        str_y = pad_with_zeros_to_right(str_y, n)
        
        
        #divide the numbers into 4 parts, 2 parts from each
        a = divide_by_10(str_x,nby2)
        b = mod_by_10(str_x,nby2)
        c = divide_by_10(str_y,nby2)
        d = mod_by_10(str_y,nby2)
        
        f.write("----------------------------\n")
        f.write("Intermediate Values of A1, B1 after partition:\n")
        f.write("----------------------------\n")
        f.write("A:"+str_x+" A1: "+a+" A2: "+b+"\n")
        f.write("B:"+str_y+" B1: "+c+" B2: "+d+"\n")
        
        #multiply each parts seperately using recursive call
        ac = large_multiply(a,c,f)
        bd = large_multiply(b,d,f)
        ad_plus_bc = add(str(large_multiply(a, d,f)),str(large_multiply(b, c,f)))
         
        # writing n as 2*nby2 takes care of both even and odd n
        prod = add(add(multiply_by_10(ac, 2*nby2) , multiply_by_10(ad_plus_bc, nby2)), bd)
        
        #remove the extra padding added by 10 multiplication
        prod=prod[:len(prod)-x_padding-y_padding]
        
        return prod

def divide_by_10(x,num_of_zeros):
    return x[:len(x)-num_of_zeros]

def mod_by_10(x,num_of_zeros):
    return x[len(x)-num_of_zeros:]

def multiply_by_10(x,num_of_zeros):
    return x+"0"*num_of_zeros

def add(x,y):
    n = max(len(x),len(y))
    
    x = pad_with_zeros(x, n)
    y = pad_with_zeros(y, n)
    
    pos = n-1
    carry=0
    ans=""
    
    #loop through the digits to add them individually
    while(pos>=0):
        x_digit = int(x[pos])
        y_digit = int(y[pos])
        sum = x_digit + y_digit + carry
        ans = str(sum%10) + ans
        carry = int(sum/10) 
        pos=pos-1
    if carry>0:
        ans=str(carry)+ans
    return ans

def pad_with_zeros(x, n):
    if n > len(x):
        num_of_zeros = n-len(x)
        return "0"*num_of_zeros+x
    else:
        return x

def pad_with_zeros_to_right(x, n):
    if n > len(x):
        num_of_zeros = n-len(x)
        return x+"0"*num_of_zeros
    else:
        return x

def main():
    lines = ""
    f= open("outputPS2.txt","w")

    with open("inputPS2.txt", encoding='utf8') as fin:
        lines = fin.read().strip()
    splitLines = lines.split("\n")
    num1 = splitLines[0]
    num2 = splitLines[1]
    f.write("1st Number, A:"+num1+"\n")
    f.write("2nd Number, B:"+num2+"\n")
    
    ans=large_multiply(num1, num2, f)
    f.write("----------------------------\n")
    f.write("Result:> "+num1+" x "+num2+" = "+ans+"\n")
    f.write("----------------------------\n")
    
if __name__== "__main__":
    main()
