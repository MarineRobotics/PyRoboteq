#!/user/bin/env python

import sys
#from roboteq_ros.PyRoboteq.roboteq_handler import RoboteqHandler
#import roboteq_ros.PyRoboteq.roboteq_21_commands as cmd

from PyRoboteq.roboteq_handler import RoboteqHandler
import PyRoboteq.roboteq_21_commands as cmd
import time



def read_info(roboteq: RoboteqHandler):
    # Read and print motor position and current
    print("Motor 1 position: ", roboteq.read_value(cmd.READ_FEEDBACK, 1))
    #print("Motor 2 position: ", roboteq.read_value(cmd.READ_FEEDBACK, 2))
    print("Motor 1 current: ", roboteq.read_value(cmd.READ_MOTOR_AMPS, 1))
    #print("Motor 2 current: ", roboteq.read_value(cmd.READ_MOTOR_AMPS, 2))

if __name__ == '__main__':
    roboteq = RoboteqHandler(debug_mode=True)
    # Get the port from the run variable
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        print("No port specified, using default port /dev/ttyUSB0")
        port = '/dev/ttySC0'
    roboteq.connect(port)

    # while loop, some code executes at 10hz, some at 1hz
    counter = 0

    # Define the frequencies of the code execution
    freq_10hz = 10
    freq_2hz = 2
    freq_1hz = 1

    left = -1000
    right = 1000
    increment = 500
    motor_pos = 0

    enable = roboteq.read_value(cmd.ECHO_ENABLE_DISABLE, 1)
    #print enable in red
    print("\033[91m Enable: ", enable, "\033[0m")

    # STOP all motors
    roboteq.send_command(cmd.STOP_ALL_MODES, 1)



    # Desired frequencies in Hz
    freq_fastest = 10
    freq_mid = 1
    freq_slow = 0.5

    # Interval durations in seconds
    interval_fast = 1 / freq_fastest
    interval_mid = 1 / freq_mid
    interval_slow = 1 / freq_slow

    # Initialize timers
    timer1 = time.time()
    timer2 = time.time()
    timer3 = time.time()

    try:
        while True:
            current_time = time.time()

            # Code executing at 10 Hz
            if current_time - timer1 >= interval_fast:
                #print("Code executing at 10 Hz")
                #roboteq.send_command(cmd.GO_TO_SPEED_POS, 1, motor_pos)
                #status = roboteq.read_value(cmd.READ_RUNTIME_STATUS_FLAG, 1)
                status = roboteq.read_line()
                # print status in green
                print("\033[92m Status: ", status, "\033[0m")
                
                timer1 = current_time

            # Code executing at 2 Hz
            if current_time - timer2 >= interval_mid:
                #print("Code executing at 2 Hz")
                #read_info(roboteq)
                amp_cmd = f"{cmd.READ_MOTOR_AMPS} 1"
                runtime_cmd = f"{cmd.READ_RUNTIME_STATUS_FLAG} 1"
                feedback_cmd = f"{cmd.READ_FEEDBACK} 1"
                roboteq.send_raw_command(amp_cmd)
                roboteq.send_raw_command(runtime_cmd)
                roboteq.send_raw_command(feedback_cmd)
                timer2 = current_time
                motor_cmd = f"{cmd.GO_TO_SPEED_POS} 1 {motor_pos}"
                roboteq.send_raw_command(motor_cmd)

            # Code executing at 1 Hz
            if current_time - timer3 >= interval_slow:
                #print("Code executing at 1 Hz")                
                if motor_pos == right or motor_pos == left:
                    increment = -increment
                motor_pos += increment
                timer3 = current_time

            # Sleep for a short duration to reduce CPU usage
            time.sleep(0.001)
    except KeyboardInterrupt:
        print("Exiting...")
        quit()

        # explain the difference between quit() and sys.exit()




    try:
        while True:
            # Execute the code at 10 Hz
            if counter % freq_10hz == 0:
                # Do something
                # Print motor_pos in purple
                print("\033[95mMotor position: ", motor_pos, "\033[0m")
                roboteq.send_command(cmd.GO_TO_SPEED_POS, 1, motor_pos)
                
            # Execute the code at 2 Hz
            if counter % freq_2hz == 0:
                # Do something else
                read_info(roboteq)
            # Execute the code at 1 Hz
            if counter % freq_1hz == 0:
                # Do something else entirely
                if motor_pos >= 1000:
                    motor_pos = left
                else:
                    motor_pos += 1000
            # Increment the counter
            counter += 1

            # Sleep for 1/freq_10hz seconds
            sleep(1 / freq_10hz)
    except KeyboardInterrupt:
        print("Exiting...")

