import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

class SmartMCP:
    def __init__(self):
        self.p=2
    def read(MCP3008, pin):
        mcp=Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(0,0)).read_adc(pin)
        
        return mcp