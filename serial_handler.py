import serial
import threading
from queue import Queue, Empty

class SerialHandler:
    def __init__(self, port='/dev/ttySC0', baudrate=115200, debug_mode = False):
        self.port = port
        self.baudrate = baudrate
        self.serial_connection = serial.Serial(self.port, self.baudrate, timeout=1)
        self.debug_mode = debug_mode

        self.write_queue = Queue()
        self.read_queue = Queue()

        self.stop_threads = threading.Event()

        self.write_thread = threading.Thread(target=self.write_serial)
        self.read_thread = threading.Thread(target=self.read_serial)

        self.write_thread.start()
        self.read_thread.start()

    def write_serial(self):
        while not self.stop_threads.is_set():
            try:
                data = self.write_queue.get(timeout=1)
                self.serial_connection.write(data.encode())
            except Empty:
                continue

    def read_serial(self):
        while not self.stop_threads.is_set():
            try:
                line = self.serial_connection.read_until(b'\r').decode()
                if self.debug_mode:
                    print(f"DEBUG MODE: Rx:{line}")
                self.read_queue.put(line)
            except Exception as e:
                if self.debug_mode:
                    print("DEBUG MODE: Failed to read from the controller, read the exception error below:")
                    print(e)
                    print("\n")
                else:
                    pass

    def send_data(self, data):
        self.write_queue.put(data)

    def get_data(self):
        try:
            return self.read_queue.get_nowait()
        except Empty:
            return None

    def stop(self):
        self.stop_threads.set()
        self.write_thread.join()
        self.read_thread.join()
        self.serial_connection.close()

# Usage example:
if __name__ == "__main__":
    import time

    serial_handler = SerialHandler()

    try:
        while True:
            serial_handler.send_data('Hello World')
            time.sleep(1)
            data = serial_handler.get_data()
            if data:
                print(f"Received data: {data}")
    except KeyboardInterrupt:
        serial_handler.stop()
