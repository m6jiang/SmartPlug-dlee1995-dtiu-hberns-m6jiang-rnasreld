import sqlite3
from main import getsensor
conn = sqlite3.connect('sensor.db')
dhtPin = 4
mcpPin = 2

class SmartSoundSQL:
    c = conn.cursor()
    c.execute('''CREATE TABLE sound
                 (audio,envelope,gate)''')
    c.execute("INSERT INTO sound VALUES (newSS.get_audio())newSS.get_envelope()),newSS.get_gate())")
    conn.commit()
    conn.close()

class MCPSQL:
    c = conn.cursor()
    c.execute('''CREATE TABLE MCP
                 (MCP)''')
    c.execute("INSERT INTO MCP VALUES (newMCP.read(mcpPin)))")
    conn.commit()
    conn.close()

class DHTSQL:
    c = conn.cursor()
    c.execute('''CREATE DHT
                 (temp_c,temp_f,humidity)''')
    c.execute("INSERT INTO DHT VALUES (newDHT.get_temp_celsius()),newDHT.get_temp_fahrenheit()),newDHT.get_humidity()))")
    conn.commit()
    conn.close()


