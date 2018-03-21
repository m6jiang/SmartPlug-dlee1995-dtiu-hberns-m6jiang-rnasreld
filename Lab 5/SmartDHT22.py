import Adafruit_DHT

class SmartDHT:
    def __init__(self,pin):
        humidity, temperature_C = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pin)
        
    def get_temp_celsius(SmartDHT):
        pin = 4
        humidity, temperature_C = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pin) 
        
        return temperature_C
    
    def get_temp_fahrenheit(SmartDHT):
        pin = 4
        humidity, temperature_C = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pin)
        temperature_F = temperature_C *9/5.0 + 32
        
        return temperature_F
    
    def get_humidity(SmartDHT):
        pin = 4
        humidity, temperature_C = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pin)
        
        return humidity
