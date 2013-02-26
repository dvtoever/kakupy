from __future__ import division
import RPi.GPIO as GPIO

class Unit: 
  def __init__(self, unitCode, id):
    self.unitCode = unitCode
    self.id = id

class Sender:
  shortSleep = 226  / 1000000
  longSleep  = 1600 / 1000000
  startSleep = 3300 / 1000000

  def __init__(self, outputPin):
    self.outputPin = outputPin

  def __sendStart(self):
    GPIO.output(self.outputPin, True)
    time.sleep(self.shortSleep)
    GPIO.output(self.outputPin, False)
    time.sleep(self.startSleep)

  def __sendPulse0(self):
    GPIO.output(self.outputPin, True)
    time.sleep(self.shortSleep)
    GPIO.output(self.outputPin, False)    
    time.sleep(self.shortSleep)

  def __sendPulse1(self):
    GPIO.output(self.outputPin, True)
    time.sleep(self.shortSleep)
    GPIO.output(self.outputPin, False)
    time.sleep(self.longSleep)

  def __sendHigh(self):
    self.__sendPulse0()
    self.__sendPulse1()
 
  def __sendLow(self):
    self.__sendPulse1()
    self.__sendPulse0()

  def __sendId(self, id):
    binaryIdStr = "{0:b}".format(id)
    idLength = len(binaryIdStr)

    # 26 posities, opvullen met hoge pulsen
    for i in range(26-idLength):
      self.__sendHigh()

    for j in range(idLength):
      if binaryIdStr[j] == '1':
        self.__sendLow()
      else:
        self.__sendHigh()
 

  def turnOff(self, unit):
    self.__sendStart()
    self.__sendId(unit.id)
    self.__sendHigh(); 
    


if __name__ == '__main__':
    import sys, time

    senderPin = 11
    
    #Setup WiringPi
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(senderPin, GPIO.OUT)

    lamp = Unit(2, 8983502)
    sender = Sender(senderPin)

    sender.turnOff(lamp)

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
