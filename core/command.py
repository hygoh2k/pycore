import os


class CoreCommand:
    
    def __init__(self, name="", default_status= -1):
        self.name = name
        self.status = default_status

    def execute(self):
        self.status = 0
    
        

class DummyPassCommand(CoreCommand):
    def __init__(self):
        super().__init__()

    def execute(self):
        print(f"Start Command")

class UsbCommand(CoreCommand):
    def __init__(self, port, signal):
        self.port = port
        self.signal = signal
        super().__init__()

    def execute(self):
        self.status = 0
        print(f"[Command] Execute Usb Command with Port {self.port} and Signal {self.signal} ... Status:{'PASS' if self.status == 0 else 'FAIL'}")
        
        
        



if __name__ == "__main__":
    cmdRepo = []
    cmdRepo.append(CoreCommand())
    cmdRepo.append(UsbCommand(3,0))
    cmdRepo.append(DummyPassCommand())
    
    for cmd in cmdRepo:
        cmd.execute()
        print(cmd.status)
