import time
import serial

# Define the virtual serial port names
port_send = "/dev/tnt0"


ser_send = serial.Serial(
    port_send,
    9600,
    bytesize=serial.EIGHTBITS,
    stopbits=serial.STOPBITS_ONE,
    parity=serial.PARITY_NONE,
    timeout=3
    )

try:
    counter = 0
    while True:

        # Data to send (simulating live data)
        data_to_send = "Live data: " + str(counter) + "\r\n"
        counter += 1

        # Send data to the virtual device
        ser_send.write(data_to_send.encode())
        ser_send.flush()  

        time.sleep(1)

except Exception as e:
    print(f"An Error has occoured: {e}")
    ser_send.close()
