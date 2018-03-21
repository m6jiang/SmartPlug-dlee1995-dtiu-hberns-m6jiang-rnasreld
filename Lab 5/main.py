import requests
import sys
import time
import SmartMCP3008
import SmartDHT22
import SmartSound
import json

dhtPin = 4
mcpPin = 2

newSound = SmartSound.SmartSound()
newMCP = SmartMCP3008.SmartMCP()
newDHT = SmartDHT22.SmartDHT(dhtPin)


def add_data():
    url = "http://100.80.242.4:5000/data_post"
    values = {"tempC" : newDHT.get_temp_celsius(), "tempF" : newDHT.get_temp_fahrenheit(), "light" : newMCP.read(mcpPin), "humidity" : newDHT.get_humidity(), "envelope" : newSound.get_envelope()}
    print(values)
    valJSON=json.dumps(values)
    return requests.post(url, data=valJSON)
    
    
while 1:
    add_data()
    print("data added")
    time.sleep(60)
     
                                                      



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
