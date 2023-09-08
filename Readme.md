# Emulate Serial port using tty0tty and Pyserial

## 1. Setup virtual ports using tty0tty

Use the steps mentioned in [tty0tty readme](https://github.com/lcgamboa/tty0tty) and setup tty0tty
This would open up virtual ports

```
/dev/tnt0  <->  /dev/tnt1
/dev/tnt2  <->  /dev/tnt3
/dev/tnt4  <->  /dev/tnt5
/dev/tnt6  <->  /dev/tnt7
```

Any data send to any of the above pairs would be echoed to its paired port.

## 2. Install PySerial package

`pip install pyserial`

## 3. Run send_data.py

Edit the file send_data.py to your needs. It is currently set to send just incremented numbers to simulate a live data.

## 4. Run receive_data.py

Currently the program is set to print out what it is receiving from the port and wirte the results to a file named `received_data.txt`
