import serial
import time
try:
    import roboteq_ros.PyRoboteq.roboteq_21_commands as cmd
except ModuleNotFoundError:
    from . import roboteq_21_commands as cmd
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
                bytesize= serial.EIGHTBITS
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

    def send_raw_string(self, str_command: str = "") -> None:
        """
        Send a raw string command, the library will handle sending the command, but how you write it
        is up to you.
        """
        raw_command = f"{str_command}+\r"
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
        

    def request_handler(self, request: str = "") -> str:
        """
        Sends a command and a parameter, 
        """
        def get_data(serial):
            raw_data = b''
            while raw_data == b'':
                try:
                    raw_data = serial.read_all()
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

        self.send_raw_string(request)
        result = get_data(self.ser)
        result = result.decode()
        result = result.split("\r")
        try:
            return result[1]
        
        except IndexError: # will raise index error as sometimes the controller will return an odd answer, its rare, so its simply ignored.
            debug_return = "DEBUG MODE: Received faulty message, ignoring..."
            if self.exit_on_interrupt:
                quit()
            if self.debug_mode:
                print(debug_return)
            return debug_return


    def send_command(self, command: str, first_parameter = "", second_parameter = "") -> None:
        message = f"{command} {first_parameter} {second_parameter}"

        try:
            self.send_raw_string(message)
        except Exception as e:
            if self.debug_mode:
                print("DEBUG MODE: Failed to construct a message, read the exception error below:")
                print(e)
                print(f"Received exception: {e}")
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
        request = f"{command} [{parameter}]"
        response = self.request_handler(request)
        return response

    def set_motor1_position(self, position: int) -> None:
        """
        Set the position of motor 1.
        :param position: Absolute count destination for motor 1, signed 32-bit integer from -2147M to +2147M.
        """
        command = f"{cmd.GO_TO_ABS_POS} 1 {position}"
        self.send_command_request(command)

    def set_motor2_position(self, position: int) -> None:
        """
        Set the position of motor 2.
        :param position: Absolute count destination for motor 2, signed 32-bit integer from -2147M to +2147M.
        """
        command = f"{cmd.GO_TO_ABS_POS} 2 {position}"
        self.send_command_request(command)
