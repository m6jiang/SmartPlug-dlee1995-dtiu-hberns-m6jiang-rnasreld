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
newSound = SmartMCP3008.SmartSound()

tempc = []
tempf = []
light = []
hum = []
env = []

for i in range(0,60):
    tempf.append(newDHT.get_temp_fahrenheit())
    tempc.append(newDHT.get_temp_celsius())
    light.append(newMCP.read(mcpPin))
    hum.append(newDHT.get_humidity())
    env.append(newSound.get_envelope())
    #time.sleep(0.1)

c = json.dumps(tempf)
tf = json.dumps(tempc)
l = json.dumps(light)
h = json.dumps(hum)
e = json.dumps(env)

with open('test.json','w') as f:
    f.write(c)
    f.write(tf)
    f.write(l)
    f.write(h)
    f.write(e)
print("done")
