
from core.command import *
from core.workflow import *






if __name__ == "__main__":
    
    core_cmd = CoreCommand()
    relay_on_cmd = UsbCommand(port=3,signal=1)
    relay_off_cmd = UsbCommand(port=3,signal=0)
    
    curr_workflow = Workflow("Workflow1", relay_on_cmd, max_retry_number=3, delay_s = 3)
    next_workflow = Workflow("Workflow2", relay_off_cmd, max_retry_number=0, delay_s = 3)
    curr_workflow.destination['FAIL'] = None
    curr_workflow.destination['PASS'] = next_workflow
    
    curr_workflow.execute()