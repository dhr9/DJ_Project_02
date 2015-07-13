squares = []
for i in range(1,1000) :
    l = i*i
    squares.append(l)

    
def is_perfect_square(n) :
    if(n in squares) :
        return True
    else :
        return False
   
##def four_squares() :
##    pairs = []
##    for a in range(9999,1000000) :
##        print a
##        for b in range(999,10000)  :
##            if(is_perfect_square(a+b) == True) :
##                pairs.append([a,b])
##    return pairs

def sum_of_squares(n) :
    for i in range(len(squares)) :
        for j in range(i,len(squares)) :
            if(squares[i] + squares[j] == n) :
                return True
    return False


def start() :
    j = []
    l = squares
    ans = []
    for i in range(len(l)) :
        if(sum_of_squares(l[i]) == True) :
            j.append(l[i])
    
    for i in range(len(j)) :
        ans.append([j[i],numbers(j[i])])
    return ans 
        

def numbers(n) :
    l = []
    for i in range(len(squares)) :
        for j in range(i,len(squares)) :
            if(squares[i] + squares[j] == n) :
                return([squares[i],squares[j]])

def four_numbers(a,b) :
    for i in range(1,a) :
        print i
        for j in range(1,b) :
            if((i!=j) and (i!=(b-j) and ((a-i)!= j) and((a-i) != (b-j)))and 
                ((is_perfect_square(i+j)) == True) and 
               ((is_perfect_square((a-i)+j)) == True) and
               ((is_perfect_square(i+(b-j))) == True)and
               ((is_perfect_square((a-i)+(b-j))) == True)) :
                    print(str(i) + ' ' + str(a-i) + ' ' + str(j) + ' ' + str(b-j))
                    return True
    return False

 
