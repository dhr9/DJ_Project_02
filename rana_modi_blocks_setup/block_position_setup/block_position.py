##import dynamixel.py
##import arduino.py
import math

def block_values(s) : 
    a=25
    b=25
##    l = [float(raw_input('alpha_1 ?')),float(raw_input('beta_1 ?'))]
    p=[0, 0, 0 ,0, 0, 0, 1]
##    alpha1,beta1,alpha2,beta2,s1,s2,flag

    print("TURN OFF DYNAMIXEL POWER AND GO TO THE REQUIRED POSITION")
    print("press any key to continue AFTER TURNING POWER BACK ON")
    raw_input()
    #l = dynamixel.position_read()          # UNCOMMENT LATER
    print("dynamixel position read")
    l = [120,25]                            # COMMENT LATER

##    alpha_1 = l[0]
##    beta_1 = l[1]
##    print alpha_1, beta_1


    def calc_when_negative_angles(alpha_1, beta_1):
    ##    s1 = int(raw_input('rana value daal of s1'))
    ##    alpha_1 = l[0]
    ##    beta_1 = l[1]
        p[0] = alpha_1
        p[1] = beta_1
    ##    print p[0], p[1]
    ##    print(beta_1)
        x = math.sin(math.radians(beta_1))
    ##    print 'sin beta_1=',x
        y =  math.cos(math.radians(beta_1))
    ##    print 'cos beta_1=',y
    ##    print(x/((a/b)+y))
        theta = mod(math.degrees(math.atan(x/((a/b)+y))))
    ##    print 'theta=', theta2
        alpha_2 = alpha_1 - 2*theta
        p[2] = alpha_2
        beta_2 = -beta_1
        p[3] = beta_2
        p[4] = s1
        s2 = s1 - 2*(beta_1 - theta)
        s2 = s2 % 90
        p[5] = s2
           
        
    def calc_when_positive_angles(alpha_2, beta_2):
    ##    s2 = int(raw_input('rana value daal of s2'))
    ##    alpha_2 = l[0]
    ##    beta_2 = l[1]
        p[2] = alpha_2
        p[3] = beta_2
    ##    print(beta_2)
        x = math.sin(math.radians(beta_2))
    ##    print 'sin beta_2=',x
        y =  math.cos(math.radians(beta_2))
    ##    print 'cos beta_2=',y
    ##    print(x/((a/b)+y))
        theta = mod(math.degrees(math.atan(x/((a/b)+y))))
    ##    print 'theta=',theta
        alpha_1 = alpha_2 + 2*theta
        p[0] = alpha_1
        beta_1 = -beta_2
        p[1] = beta_1
        p[5] = s2
        s1 = s2 +  2*(beta_2 - theta)
        s1 = s1 % 90
        p[4] = s1
       
    def mod(angle):
        if(angle>=0):
            return angle
        if(angle<0):
            return angle*-1

    if(l[1]<0):
        alpha_1 = l[0]
        beta_1 = l[1]
        s1 = s
        calc_when_negative_angles(alpha_1, beta_1)
    else:
        alpha_2 = l[0]
        beta_2 = l[1]
        s2 = s
        calc_when_positive_angles(alpha_2, beta_2)

    print(p)

    print("CALCULATIONS COMPLETE")
    print("press any key to continue")
    print("NOTE :- PLEASE CLEAR AWAY FROM THE 'ZONE' ")
    raw_input()
    
block_values(45)

if (
