import os
import time


class Workflow:
    def __init__(self, name, command, delay_s = 0, max_retry_number = 0):
        self.name = name
        self.command = command
        self.__source = None
        self.__destination = {'PASS':None, 'FAIL':None}
        self.max_retry_number = max_retry_number
        self.delay_s = delay_s
        
    def execute(self):
        print(f'[Workflow] Running Worklow {self.name}')
        status, attempted_number = -1, -1
        
        
        while status != 0 and attempted_number < self.max_retry_number:
            self.command.execute()
            print(f'[Workflow] Waiting for {self.delay_s}s...')
            time.sleep(self.delay_s)
            
            status = self.command.status
            attempted_number += 1
        
        
        if status == 0:
            if self.__destination['PASS'] is not None:
                self.__destination['PASS'].execute()
        else:
            if self.__destination['FAIL'] is not None:
                self.__destination['FAIL'].execute()
    
    @property
    def source(self):
        return self.__source
        
    @source.setter
    def source(self, source):
        self.__source = source

    @property
    def destination(self):
        return self.__destination

    @destination.setter
    def destination(self, destination):
        self.__destination = destination
        

    


#sample calling:
if __name__ == "__main__":
    from command import *
    core_cmd = CoreCommand()
    relay_on_cmd = UsbCommand(port=3,signal=1)
    relay_off_cmd = UsbCommand(port=3,signal=0)
    
    curr_workflow = Workflow("Workflow1", relay_on_cmd, max_retry_number=3, delay_s = 3)
    next_workflow = Workflow("Workflow2", relay_off_cmd, max_retry_number=0, delay_s = 3)
    curr_workflow.destination['FAIL'] = None
    curr_workflow.destination['PASS'] = next_workflow
    
    curr_workflow.execute()
