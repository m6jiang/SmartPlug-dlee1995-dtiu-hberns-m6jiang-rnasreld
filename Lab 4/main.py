import sys
import time
import SmartMCP3008
import SmartDHT22
import SmartSound

dhtPin = 4
mcpPin = 2

class getsensor:
    newSS = SmartSound.SmartSound()
    newMCP = SmartMCP3008.SmartMCP()
    newDHT = SmartDHT22.SmartDHT(dhtPin)




#newSS = SmartSound.SmartSound()
#newMCP = SmartMCP3008.SmartMCP()
#newDHT = SmartDHT22.SmartDHT(dhtPin)

#while True:
    #print("MCP reading is: ", newMCP.read(mcpPin))
    #print("DHT Celcius reading is: ", newDHT.get_temp_celsius())
    #print("DHT Farenheit reading is: ", newDHT.get_temp_fahrenheit())
    #print("DHT Humidity reading is: ", newDHT.get_humidity())
    #print("Audio reading is: ", newSS.get_audio())
    #print("Envelope reading is: ", newSS.get_envelope())
    #print("Gate reading is: ", newSS.get_gate())
    #time.sleep(1)
