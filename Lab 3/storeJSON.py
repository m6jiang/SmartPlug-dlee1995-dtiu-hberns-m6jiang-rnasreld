import json
import sys
import time
import SmartMCP3008
import SmartDHT22
import SmartSound

dhtPin = 4
mcpPin = 2

newMCP = SmartMCP3008.SmartMCP()
newDHT = SmartDHT22.SmartDHT(dhtPin)
newSound = SmartSound.SmartSound()

values = {}

for i in range(0,60):
        values[i] = {"tempC" : newDHT.get_temp_celsius(), "tempF" : newDHT.get_temp_fahrenheit(), "light" : newMCP.read(mcpPin), "humidity" : newDHT.get_humidity(), "envelope" : newSound.get_envelope()}
        time.sleep(60)

val = json.dumps(values)

with open('test.json','w') as f:
        f.write(val)
print("done")

