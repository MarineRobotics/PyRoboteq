import time
from serial_handler import SerialHandler
import PyRoboteq.roboteq_21_commands as cmd

def process_received_data(data):
    if data.startswith('F='):
        value = int(data[2:])
        return f"feedback: {value}"
    elif data.startswith('A='):
        value = int(data[2:])
        return f"current: {value}"
    elif data.startswith('FM='):
        value = int(data[3:])
        return f"runtime status: {value}"
    else:
        return ""


def main():
    serial_handler = SerialHandler(port="/dev/ttySC0", baudrate=115200, debug_mode=False)

    left = -1000
    right = 1000
    increment = 500
    motor_pos = 0

    try:
        start_time_1hz = time.time()
        start_time_5hz = time.time()

        amp_cmd = f"{cmd.READ_MOTOR_AMPS} 1"
        runtime_cmd = f"{cmd.READ_RUNTIME_STATUS_FLAG} 1"
        feedback_cmd = f"{cmd.READ_FEEDBACK} 1"

        while True:
            current_time = time.time()
            elapsed_time_1hz = current_time - start_time_1hz
            elapsed_time_5hz = current_time - start_time_5hz

            if elapsed_time_1hz >= 1:  # Send a motor_cmd message every second
                if motor_pos == right or motor_pos == left:
                    increment = -increment
                motor_cmd = f"{cmd.GO_TO_SPEED_POS} 1 {motor_pos}"
                motor_pos += increment
                serial_handler.send_data(f"{amp_cmd}\r")
                serial_handler.send_data(f"{runtime_cmd}\r")
                serial_handler.send_data(f"{motor_cmd}\r")
                start_time_1hz = current_time

            if elapsed_time_5hz >= 0.2:  # Send amp_cmd, runtime_cmd, feedback_cmd at 5 Hz
                serial_handler.send_data(f"{feedback_cmd}\r")
                start_time_5hz = current_time

            data = serial_handler.get_data()
            if data:
                print(process_received_data(data))

            time.sleep(0.1)  # 10 Hz loop rate

    except KeyboardInterrupt:
        pass
    finally:
        serial_handler.stop()

if __name__ == "__main__":
    main()
