def only_number(s) :                #this function will take a string (eg : '0xff') and
    s1 = []                         #return only the numbers after the 0x ('ff' in this case)
    i = 0
    while(i <= len(s)) :
        n = 0
        if((s[i] == 0) and (s[i+1] == 'x')) :
            i += 2
            n = 1
        if(n != 1) :
            s1.append(s[i])
            i += 1
    s2 = s1[0]
    for i in range(1,len(s1)) :
        s2 += s1[i]
    return s2
            
