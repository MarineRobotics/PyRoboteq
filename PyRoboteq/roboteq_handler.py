import serial
import time
# message
class RoboteqHandler:
    """
    Create a roboteq device object for communication, read the README for more information
    param: exit_on_interrupt - exits program with any error received (recommended for debugging)
    param: debug_mode - prints every data sent to the controller and received from the controller, doesnt stop the program.
    """

    def __init__(self, exit_on_interrupt = False, debug_mode = False):
        self.is_alive = False
        self.port = ""
        self.baudrate = 115200
        self.ser = None
        self.exit_on_interrupt = exit_on_interrupt
        self.debug_mode = debug_mode
    
    def connect(self, port: str, baudrate: int = 115200) -> bool:
        """
        Attempt to establish connection with the controller
        If the attempt fails, the method will return False otherwise, True.

        """
        self.port = port
        self.baudrate = baudrate
        
        if self.debug_mode:
            print(f"DEBUG MODE: {self.debug_mode}")
            print(f"EXIT ON INTERRUPT: {self.exit_on_interrupt}")
            time.sleep(1)

        try: # attempt to create a serial object and check its status
            self.ser = serial.Serial(
                port = self.port,
                baudrate = self.baudrate,
                parity = serial.PARITY_NONE,
                stopbits = serial.STOPBITS_ONE,
                bytesize= serial.EIGHTBITS,
                timeout = 0.1,
                write_timeout = 1
            )
            if self.ser.isOpen():
                self.ser.close()
            self.ser.open()
            self.is_alive = True

        except Exception as e:
            if self.debug_mode:
                print("DEBUG MODE: ERROR: Failed to connect to the roboteq device, read the exception error below:")
                print(e)
                print("\n")
            self.is_alive = False
            
        return self.is_alive

    def send_raw_command(self, str_command: str = "") -> None:
        """
        Send a raw string command, the library will handle sending the command, but how you write it
        is up to you.
        """
        raw_command = f"{str_command}\r"
        try:
            if self.debug_mode:
                print(f"DEBUG MODE: Tx:{raw_command}")
            self.ser.write(raw_command.encode())

        except Exception as e:
            if self.debug_mode:
                print("DEBUG MODE: Failed to send command to the controller, read the exception error below:")
                print(e)
                print("\n")
            if self.exit_on_interrupt:
                quit()

    def read_line(self) -> str:
        """
        Reads a line from the controller, the line is terminated with a carriage return (\r)
        """
        try:
            raw_data = self.ser.read_until(b'\r')
            if self.debug_mode:
                print(f"DEBUG MODE: Rx:{raw_data}")
            return raw_data.decode()
        except Exception as e:
            if self.debug_mode:
                print("DEBUG MODE: Failed to read from the controller, read the exception error below:")
                print(e)
                print("\n")
            if self.exit_on_interrupt:
                quit()
            return ""

        
    def request_handler(self, request: str = "") -> str:
        """
        Sends a command and a parameter, 
        """
        def get_data(serial):
            raw_data = b''
            while raw_data == b'':
                try:
                    #raw_data = serial.read_all()
                    raw_data = serial.read_until(b'\r')
                except Exception as e:
                    if self.debug_mode:
                        print("DEBUG MODE: Failed to read from the controller, read the exception error below:")
                        print(e)
                        print("\n")
                    if self.exit_on_interrupt:
                        quit()
                    raw_data = b' '
            
            if self.debug_mode:
                print(f"DEBUG MODE: Rx:{raw_data}")
            return raw_data
        #self.ser.read_all()
        self.send_raw_command(request)
        result = get_data(self.ser)
        # print result in purple
        print("\033[95m {}\033[00m" .format(result))
        result = result.decode()
        # print result in blue
        print("\033[94m {}\033[00m" .format(result))
        #result = result.split("\r")
        # print result in green
        #print("\033[92m {}\033[00m" .format(result))
        try:
            return result[1]
        
        except IndexError: # will raise index error as sometimes the controller will return an odd answer, its rare, so its simply ignored.
            debug_return = "DEBUG MODE: Received faulty message, ignoring..."
            if self.exit_on_interrupt:
                quit()
            if self.debug_mode:
                print(debug_return)
            return debug_return

    def dual_motor_control(self, left_motor: int = 0, right_motor: int = 0) -> None:
        """
        Controlling the motor using a Dual Drive mode
        Send speed for the left, and right side of the robot/vehicle seperately 
        Effective for doing Pivot drive and running track based robots
        left_motor: integer from -1000 to 1000
        right_motor: integer from -1000 to 1000
        """
        raw_command = f"!M {left_motor} {right_motor} "
        self.request_handler(raw_command)
    
    def send_command(self, command: str, first_parameter = "", second_parameter = "") -> None:
        message = f"{command} {first_parameter} {second_parameter}".strip()

        try:
            # serial read all
            self.ser.read_all()
            response = self.request_handler(message)
        except Exception as e:
            if self.debug_mode:
                print("DEBUG MODE: Failed to construct a message, read the exception error below:")
                print(e)
                print(f"Received message: {response}")
                print("\n")
            if self.exit_on_interrupt:
                quit()

    def read_value(self, command: str = "", parameter = "") -> str:
        """
        Constructs a message and sends it to the controller.
        param: command (str)
        param: parameter (str/int)
        returns: answer from the controller, data from request commands, or echo from action commands.
        """
        request = f"{command} {parameter}"
        response = self.request_handler(request)
        return response