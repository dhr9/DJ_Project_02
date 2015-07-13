'''this file generates the not checksum of for the instruction packet for sending
        int to the dynamixel '''

def only_number(s) :
    s1 = (s[2])
    for i in range(3,len(s)) :
        s1 += s[i]
    print 'okay only_number'
    print(s1)
    return s1
                                        #            only_number(s) 
def byte(s) :                           #                   |
    if(len(s) < 8) :                    #                   |
        s1 = ''                         #                   |
        for i in range(10-len(s)) :     #                   \/
            s1 += '0'                   #                 byte(s)
        for i in range(2,len(s)) :      #                   |
            s1 += s[i]                  #                   |
        print 'okay byte'               #                   |
        print(s1)                       #                   \/
        return s1                       #              check_length(s)
    else :                              #                   |       |
        print 'okay byte'               #                   |       |
        return s                        #                   |       |
                                        #                   \/      |
                                        #               byte_not(s) |
def byte_not(s) :                       #                   |       |
    s1 = ''                             #                   |       |
    b = '0'                             #                   |       |
    for i in range(len(s)) :            #                   \/      \/
        if(s[i] == '0') :               #                  byte_not(s)
            b = '1'                     #                   |
        else :                          #                   |
            b = '0'                     #                   |
        s1 += b                         #                   \/
    print 'okay byte_not'               #                 int(s,2)
    print(s1)                           #                   |
    return s1                           #                   |
                                        #                   |
def check_length(s) :                   #                   \/
    l = len(s)                          #               not_checksum(n)
    if(l > 8) :                         #
        print 'okay check_len'          #
        print 'going to trim_len'       #
        return trim_len(s)              #
    else :                              #
        print 'okay check_len'
        print(s)
        return s

def trim_len(s) :
    s1 = ''
    for i in range((len(s)-8),len(s)) :
        s1 += s[i]
    print 'okay trim_len'
    print(s1)
    return s1

def notchecksum(n) :
    binary = (byte_not(check_length(byte(only_number(bin(n))))))
    integer = int(binary,2)
    return integer
