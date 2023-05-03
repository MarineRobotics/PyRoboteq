# This file contains the full list of the commands used by the SDC21** motor driver series
# Each constant will be used as a message receiver or sender parameter (Send speed, read speed, etc..)

# These commands have been based on V2.2 of the Roboteq SDC21xx manual, .
# You can refer to the download section of the Roboteq website for the latest version of the manual:
# https://www.roboteq.com/support/documentation-downloadn

# NOTICE: These constants are for serial use

# Runtime Commands
SET_ACCEL = "!AC"      # Set Acceleration
NXT_ACCEL = "!AX"      # Next Acceleration
SET_BOOL = "!B"        # Set User Boolean Variable
SPECTRUM_BIND = "!BND" # Spectrum Bind
SET_ENC_COUNT = "!C"   # Set Encoder Counters
SET_BL_COUNT = "!CB"   # Set Brushless Counter
SET_MOTOR_CAN = "!CG"  # Set Motor Command via CAN
CAN_SEND = "!CS"       # CAN Send
SET_SSI_COUNTER = "!CSS" # Set SSI Sensor Counter
RAW_REDIRECT_SEND = "!CU" # Raw Redirect Send
RESET_DIG_OUT_BIT = "!D0" # Reset Individual Digital Out bits
SET_DIG_OUT_BIT = "!D1"  # Set Individual Digital Out bits
SET_DECEL = "!DC"        # Set Deceleration
SET_ALL_DIG_OUT = "!DS"  # Set all Digital Out bits
NEXT_DECEL = "!DX"       # Next Decceleration
SAVE_CONFIG_EEPROM = "!EES" # Save Configuration in EEPROM
EMERGENCY_SHUTDOWN = "!EX"  # Emergency Shutdown
GO_TO_SPEED_POS = "!G"      # Go to Speed or to Relative Position
GO_TO_TORQUE_AMPS = "!GIQ"  # Go to Torque Amps
GO_TO_FLUX_AMPS = "!GID"    # Go to Flux Amps
LOAD_HOME_COUNTER = "!H"    # Load Home counter
EMERGENCY_STOP_RELEASE = "!MG" # Emergency Stop Release
STOP_ALL_MODES = "!MS"      # Stop in all modes
GO_TO_ABS_POS = "!P"         # Go to Absolute Desired Position
GO_TO_REL_POS = "!PR"        # Go to Relative Desired Position
NEXT_GO_TO_REL_POS = "!PRX"  # Next Go to Relative Desired Position
NEXT_GO_TO_ABS_POS = "!PX"   # Next Go to Absolute Desired Position
MICROBASIC_RUN = "!R"        # MicroBasic Run
SET_PULSE_OUT = "!RC"        # Set Pulse Out
SET_MOTOR_SPEED = "!S"       # Set Motor Speed
SAFETY_STOP = "!SFT"         # Safety Stop
STO_SELF_TEST = "!STT"       # STO Self-Test
NEXT_VELOCITY = "!SX"        # Next Velocity
SET_USER_VAR = "!VAR"        # Set User Variable

# Runtime Queries
READ_MOTOR_AMPS = "?A"                       # Read Motor Amps
READ_ANALOG_INPUTS = "?AI"                   # Read Analog Inputs
READ_ANALOG_INPUT_CONVERSION = "?AIC"        # Read Analog Input after Conversion
READ_ROTOR_ANGLE = "?ANG"                    # Read Rotor Angle
READ_RAW_SIN_COS_SENSOR = "?ASI"             # Read Raw Sin/Cos sensor
READ_USER_BOOL_VAR = "?B"                    # Read User Boolean Variable
READ_BATTERY_AMPS = "?BA"                    # Read Battery Amps
READ_BRUSHLESS_COUNT_REL = "?BCR"            # Read Brushless Count Relative
READ_BL_MOTOR_RPM = "?BS"                    # Read BL Motor Speed in RPM
READ_BATTERY_SOC_PERCENT = "?BSC"            # Read Battery State of Charge in percentage
READ_BL_MOTOR_RPM_FRACTION = "?BSR"          # Read BL Motor Speed as 1/1000 of Max RPM
READ_BATTERY_SOC_AMP_HOURS = "?BMC"          # Read Battery State Of Charge in AmpHours
READ_BMS_STATUS_FLAGS = "?BMF"               # Read BMS Status Flags
READ_BMS_SWITCH_STATES = "?BMS"              # Read BMS Switch States
READ_ENCODER_COUNT_ABS = "?C"                # Read Encoder Counter Absolute
READ_RAW_CAN_FRAME = "?CAN"                  # Read Raw CAN frame
READ_ABS_BRUSHLESS_COUNTER = "?CB"           # Read Absolute Brushless Counter
READ_RAW_REDIRECT_RECEIVED_COUNT = "?CD"     # Read Raw Redirect Received Frames Count
READ_RAW_CAN_RECEIVED_COUNT = "?CF"          # Read Raw CAN Received Frames Count
READ_CAN_CONSUMER_HEARTBEAT_STATUS = "?CHS"  # CAN Consumer Heartbeat Status
READ_CONVERTED_ANALOG_COMMAND = "?CIA"       # Read Converted Analog Command
READ_INTERNAL_PULSE_COMMAND = "?CIP"         # Read Internal Pulse Command
READ_INTERNAL_SERIAL_COMMAND = "?CIS"        # Read Internal Serial Command
READ_ROBOCAN_ALIVE_NODES_MAP = "?CL"         # Read RoboCAN Alive Nodes Map
READ_ENCODER_COUNT_REL = "?CR"               # Read Encoder Count Relative
READ_REL_SSI_SENSOR_COUNTER = "?CSR"         # Read Relative SSI Sensor Counter
READ_ABS_SSI_SENSOR_COUNTER = "?CSS"         # Read Absolute SSI Sensor Counter
READ_DIGITAL_INPUTS = "?D"                   # Read Digital Inputs
READ_INDIV_DIGITAL_INPUTS = "?DI"            # Read Individual Digital Inputs
READ_RAW_REDIRECT_RECEIVED_FRAME = "?DDT"    # Read Raw Redirect Received Frame
READ_DIGITAL_OUTPUT_STATUS = "?DO"           # Read Digital Output Status
READ_MOTOR_DC_PEAK_AMPS = "?DPA"             # Read Motor DC/Peak Amps
READ_DESTINATION_REACHED = "?DR"             # Read Destination Reached
READ_CLOSED_LOOP_ERROR = "?E"                # Read Closed Loop Error
READ_FEEDBACK = "?F"                         # Read Feedback
READ_FOC_ANGLE_ADJUST = "?FC"                # Read FOC Angle Adjust
READ_FLOW_SENSOR_COUNTER = "?FLW"            # Read Flow Sensor Counter
READ_FAULT_FLAGS = "?FF"                     # Read Fault Flags
READ_FIRMWARE_ID = "?FID"                    # Read Firmware ID
READ_FIRMWARE_ID_NUM = "?FIN"                # Read Firmware ID (numerical)
READ_RUNTIME_STATUS_FLAG = "?FM"             # Read Runtime Status Flag
READ_STATUS_FLAGS = "?FS"                    # Read Status Flags
READ_HALL_SENSOR_STATES = "?HS"              # Read Hall Sensor States
IS_ROBOCAN_NODE_ALIVE = "?ICL"               # Is RoboCAN Node Alive
READ_SPEKTRUM_RECEIVER = "?K"                # Read Spektrum Receiver
READ_LOCK_STATUS = "?LK"                     # Read Lock status
READ_MOTOR_COMMAND_APPLIED = "?M"            # Read Motor Command Applied
READ_FOC_MOTOR_AMPS = "?MA"                  # Read Field Oriented Control Motor Amps
READ_MAGSENSOR_TRACK_DETECT = "?MGD"         # Read Magsensor Track Detect
READ_MAGSENSOR_MARKERS = "?MGM"              # Read Magsensor Markers
READ_MAGSENSOR_STATUS = "?MGS"               # Read Magsensor Status
READ_MAGSENSOR_TRACK_POSITION = "?MGT"       # Read Magsensor Track Position
READ_MAGSENSOR_GYROSCOPE = "?MGY"            # Read Magsensor Gyroscope
READ_MAGSENSOR_TAPE_CROSS_DETECT = "?MGX"    # Read MagSensor Tape Cross Detection
READ_MOTOR_POWER_OUTPUT = "?P"               # Read Motor Power Output Applied
READ_PHASE_AMPS = "?PHA"                     # Read Phase Amps
READ_PULSE_INPUTS = "?PI"                    # Read Pulse Inputs
READ_PULSE_INPUT_CONVERSION = "?PIC"         # Read Pulse Input after Conversion
READ_ENCODER_MOTOR_RPM = "?S"                # Read Encoder Motor Speed in RPM
READ_SCRIPT_CHECKSUM = "?SCC"                # Read Script Checksum
READ_SENSOR_ERRORS = "?SEC"                  # Read Sensor Errors
READ_RAW_REDIRECT_RECEIVED_FRAME_STR = "?SDT" # Read Raw Redirect Received Frame as string
READ_SENSOR_ANGLE = "?SNA"                   # Read Sensor Angle
READ_ENCODER_SPEED_REL = "?SR"               # Read Encoder Speed Relative
READ_SSI_SENSOR_MOTOR_RPM = "?SS"            # Read SSI Sensor Motor Speed in RPM
READ_SSI_SENSOR_SPEED_REL = "?SSR"           # Read SSI Sensor Speed Relative
STO_SELF_TEST_RESULT = "?STT"                # STO Self-Test Result
READ_TEMPERATURE = "?T"                      # Read Temperature
READ_TIME = "?TM"                            # Read Time
READ_POSITION_REL_TRACKING = "?TR"           # Read Position Relative Tracking
READ_CONTROL_UNIT_MODEL = "?TRN"             # Read Control Unit type and Controller Model
READ_MCU_ID = "?UID"                         # Read MCU Id
READ_VOLTS = "?V"                            # Read Volts
READ_USER_INT_VAR = "?VAR"                   # Read User Integer Variable

# Maintenance Commands (corrected)
MOTOR_SENSOR_SETUP = "%CLMOD"               # Motor/Sensor Setup
RESET_CONFIG_FACTORY_DEFAULTS = "%CLRST"    # Reset configuration to factory defaults
SAVE_CALIB_FLASH = "%CLSAV"                 # Save calibrations to Flash
UPDATE_FIRMWARE_USB = "%DFU"                # Update Firmware via USB
LOAD_PARAMS_EEPROM = "%EELD"                # Load Parameters from EEPROM
DUMP_FLASH_LOG_DATA = "%EELOG"              # Dump Flash Log Data
RESET_FACTORY_DEFAULTS = "%EERST"           # Reset Factory Defaults
SAVE_CONFIG_EEPROM_MAINT = "%EESAV"         # Save Configuration in EEPROM
ERASE_FLASH_LOG_DATA = "%ERASE"             # Erase Flash Log Data
LOCK_CONFIG_ACCESS = "%LK"                  # Lock Configuration Access
RESET_CONTROLLER = "%RESET"                 # Reset Controller
SCRIPT_LOAD = "%SLD"                        # Script Load
SET_TIME = "%STIME"                         # Set Time
UNLOCK_CONFIG_ACCESS = "%UK"                # Unlock Configuration Access


# General and Safety Confiurations
ECHO_ENABLE_DISABLE = "^ECHOF"              # Enable/Disable serial echo. 1: Disable, 0: Enable