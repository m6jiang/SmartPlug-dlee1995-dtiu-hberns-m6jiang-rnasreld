import sys
import time
import SmartMCP3008
import SmartDHT22

dhtPin = 4
mcpPin = 2

newMCP = SmartMCP3008.SmartMCP()
newDHT = SmartDHT22.SmartDHT(dhtPin)

i = 1;

while True:
    print("MCP reading is: ", i, newMCP.read(mcpPin))
    print("DHT Celcius reading is: ", i, newDHT.get_temp_celcius())
    print("DHT Farenheit reading is: ", i, newDHT.get_temp_farenheit())
    print("DHT Humidity reading is: ", i, newDHT.get_humidity())

time.sleep(60)