#!/user/bin/env python

import sys
#from roboteq_ros.PyRoboteq.roboteq_handler import RoboteqHandler
#import roboteq_ros.PyRoboteq.roboteq_21_commands as cmd

from PyRoboteq.roboteq_handler import RoboteqHandler
import PyRoboteq.roboteq_21_commands as cmd
from time import sleep
from PyRoboteq import config
import serial

BAUD = 115200
USB = False
debug_mode = True
exit_on_interrupt = False


def connect(port: str, baudrate: int = 115200, debug_mode: bool = False, exit_on_interrupt: bool = False) -> bool:
    """
    Attempt to establish connection with the controller
    If the attempt fails, the method will return False; otherwise, True.
    """
    is_alive = False

    if debug_mode:
        print(f"DEBUG MODE: {debug_mode}")
        print(f"EXIT ON INTERRUPT: {exit_on_interrupt}")
        sleep(1)

    try:
        if USB:
            ser = serial.Serial(
                port=port,
                baudrate=baudrate,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS
            )
            if ser.isOpen():
                ser.close()
            ser.open()
            is_alive = True
        else:
            ser = config.config(dev=port, Baudrate=baudrate)
        return ser

    except Exception as e:
        if debug_mode:
            print("DEBUG MODE: ERROR: Failed to connect to the roboteq device, read the exception error below:")
            print(e)
            print("\n")
        is_alive = False
    return None
    

def get_data(ser):
            raw_data = b''
            while raw_data == b'':
                try:
                    #raw_data = serial.read_all()
                    raw_data = ser.Uart_ReceiveLine()
                except Exception as e:
                    if debug_mode:
                        print("DEBUG MODE: Failed to read from the controller, read the exception error below:")
                        print(e)
                        print("\n")
                    if exit_on_interrupt:
                        quit()
                    raw_data = b' '
            
            if debug_mode:
                print(f"DEBUG MODE: Rx:{raw_data}")
            return raw_data


def read_info(roboteq: RoboteqHandler):
    # Read and print motor position and current
    print("Motor 1 position: ", roboteq.read_value(cmd.READ_FEEDBACK, 1))
    #print("Motor 2 position: ", roboteq.read_value(cmd.READ_FEEDBACK, 2))
    print("Motor 1 current: ", roboteq.read_value(cmd.READ_MOTOR_AMPS, 1))
    #print("Motor 2 current: ", roboteq.read_value(cmd.READ_MOTOR_AMPS, 2))


if __name__ == '__main__':
    #roboteq = RoboteqHandler(debug_mode=True)
    
    # Get the port from the run variable
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        print("No port specified, using default port /dev/ttyUSC0")
        port = '/dev/ttySC0'
    roboteq = connect(port='/dev/ttySC0', baudrate=BAUD, debug_mode=True, exit_on_interrupt=False)
    #roboteq.connect(port)


    try:        
        
        while True:
            #read_info(roboteq)
            roboteq.Uart_SendString(cmd.READ_FEEDBACK + " 1\r")
            roboteq.Uart_SendString(cmd.READ_RUNTIME_STATUS_FLAG + " 1\r")
            roboteq.Uart_SendString("!G" + " 1 0\r")
            get_data(roboteq)
            sleep(0.1)
    except KeyboardInterrupt:
        print("Exiting...")

