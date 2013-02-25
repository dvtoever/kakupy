import RPi.GPIO as GPIO
if __name__ == '__main__':
    import sys, time

    GPIO.setwarnings(False)
    senderPin = 11

    if len(sys.argv) < 3:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(senderPin, GPIO.OUT)
        for i in [1,0,1,0,1,0,1, 0]:
            print i
            GPIO.output(senderPin, i)
            time.sleep(300 / 1000000.)
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
