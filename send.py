import RPi.GPIO as GPIO

class Sender():
    
    
if __name__ == '__main__':
    import sys
    GPIO.setwarnings(False)
   
    if len(sys.argv) < 3:
            print "usage:sudo python %s int_device int_state (e.g. '%s 2 1' switches device 2 on)" % \
                    (sys.argv[0], sys.argv[0])  
            sys.exit(1)
   
   
    # Change the key[] variable below according to the dipswitches on your Elro receivers.
    #default_key = [1,0,0,0,1]
   
    # change the pin accpording to your wiring
    #default_pin =17
    #device = RemoteSwitch(  device= int(sys.argv[1]),
    #                                                key=default_key,
    #                                                pin=default_pin)

    #if int(sys.argv[2]):
    #        device.switchOn()
    #else:
    #        device.switchOff()