import json
import sys
import time
import SmartMCP3008
import SmartDHT22
#import SmartSound

dhtPin = 4
mcpPin = 2



newMCP = SmartMCP3008.SmartMCP()
newDHT = SmartDHT22.SmartDHT(dhtPin)
#newSound = SmartMCP3008.SmartSound

with open('MCP.json','w') as f:
    json.dump(newMCP.read(mcpPin),f)
with open('temp_cel.json', 'w') as f:
    json.dump(newDHT.get_temp_celcius(),f)
with open('temp_far.json', 'w') as f:
    json.dump(newDHT.get_temp_farenheit(),f)
with open('hum.json', 'w') as f:
    json.dump(newDHT.get_humidity(),f)
