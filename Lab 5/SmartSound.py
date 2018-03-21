import SmartMCP3008

class SmartSound:
        def __init__(self):
                newMCP = SmartMCP3008.SmartMCP()
                self.mcp = newMCP

        def get_gate(self):
                pin = 4
                value = self.mcp.read(pin)
                if(value > 250):
                        return True
                else:
                        return False
        def get_envelope(self):
                pin_env = 5
                return self.mcp.read(pin_env)
        def get_audio(self):
                pin_audio = 3
                return self.mcp.read(pin_audio)
            
