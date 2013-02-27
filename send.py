from __future__ import division
from __future__ import print_function

def printf(str, *args):
  print(str % args, end='')

import wiringpi

class Unit: 
  def __init__(self, unitCode, houseId):
    self.unitCode = unitCode
    self.houseId = houseId

class Sender:

  def __init__(self, outputPin, speed):
    self.io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)
    self.io.pinMode(1, self.io.OUTPUT)
    self.outputPin = outputPin
    self.shortSleep = (2*speed)  / 1000000.0
    self.longSleep  = (12*speed) / 1000000.0
    self.startSleep = (25*speed) / 1000000.0
    self.endSleep = (100*speed)  / 1000000.0


  def __sendStart(self):
    self.io.digitalWrite(self.outputPin,self.io.HIGH)
    time.sleep(self.shortSleep)
    #printf('.')
    self.io.digitalWrite(self.outputPin,self.io.LOW)
    time.sleep(self.startSleep)

  def __sendPulse0(self):
    self.io.digitalWrite(self.outputPin,self.io.HIGH)
    time.sleep(self.shortSleep)
    #printf('.')
    self.io.digitalWrite(self.outputPin,self.io.LOW)    
    time.sleep(self.shortSleep)
    #printf('.')

  def __sendPulse1(self):
    self.io.digitalWrite(self.outputPin,self.io.HIGH)
    time.sleep(self.shortSleep)
    #printf('.')
    self.io.digitalWrite(self.outputPin,self.io.LOW)
    time.sleep(self.longSleep)
    #printf('-')

  def __sendHigh(self):
    self.__sendPulse0()
    self.__sendPulse1()
 
  def __sendLow(self):
    self.__sendPulse1()
    self.__sendPulse0()

  def __sendHouseId(self, id):
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
 
  def __sendUnitCode(self, unitCode):
    binaryUnitCodeStr = "{0:b}".format(unitCode)
    unitCodeLength = len(binaryUnitCodeStr)

    for i in range(4 - unitCodeLength):
      self.__sendHigh()

    for j in range(unitCodeLength):
      if binaryUnitCodeStr[j] == '1':
        self.__sendLow()
      else:
        self.__sendHigh()

  def __sendEnd(self):
    self.io.digitalWrite(self.outputPin,self.io.HIGH)
    time.sleep(self.shortSleep)
    #printf('.')
    self.io.digitalWrite(self.outputPin,self.io.LOW)
    time.sleep(self.endSleep)
 
  def turnOff(self, unit):
    for i in range(10):
      self.__sendStart()
      #printf('|')
      self.__sendHouseId(unit.houseId)
      #printf('|')
      self.__sendHigh(); 
      self.__sendHigh(); 
      #printf('|')
      self.__sendUnitCode(unit.unitCode)
      #printf('|')
      self.__sendEnd()
      #printf('|')

if __name__ == '__main__':
    import sys, time

    senderPin = 0
    
    lamp = Unit(2, 8983502)
    sender = Sender(senderPin, float(sys.argv[1]))

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
