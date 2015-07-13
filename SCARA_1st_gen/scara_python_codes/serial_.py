def read(ser) :
    while(ser.inWaiting() != 0) :
        ser.read()
    
