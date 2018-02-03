import sys
import time
import SmartMCP3008
import SmartDHT22

dhtPin = 4
mcpPin = 2

newMCP = SmartMCP3008.SmartMCP()
newDHT = SmartDHT22.SmartDHT(dhtPin)

while True:
    print("MCP reading is: ", newMCP.read(mcpPin))
    print("DHT Celcius reading is: ", newDHT.get_temp_celcius())
    print("DHT Farenheit reading is: ", newDHT.get_temp_farenheit())
    print("DHT Humidity reading is: ", newDHT.get_humidity())

time.sleep(60)