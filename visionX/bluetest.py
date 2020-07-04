#import serial
import getch
import bluetooth
import subprocess
#import bluetooth

#Look for all Bluetooth devices
#the computer knows about.
print ("Searching for devices...")
print ("")
#Create an array with all the MAC
#addresses of the detected devices
nearby_devices = bluetooth.discover_devices()
#Run through all the devices found and list their name
num = 0
print ("Select your device by entering its coresponding number...")
for i in nearby_devices:
	num+=1
	print (num , ": " , bluetooth.lookup_name( i ))

#Allow the user to select their Arduino
#bluetooth module. They must have paired
#it before hand.
selection = int(input("> ")) - 1
print ("You have selected "+bluetooth.lookup_name(nearby_devices[selection]))
addr = nearby_devices[selection]
print(addr)
name=bluetooth.lookup_name(nearby_devices[selection])
#Create a connection to the socket for Bluetooth
#communication
passkey = "1234" # passkey of the device you want to connect

# kill any "bluetooth-agent" process that is already running
#subprocess.call("kill -9 `pidof bluetooth-agent`",shell=True)

# Start a new "bluetooth-agent" process where XXXX is the passkey
#status = subprocess.call("bluetooth-agent " + passkey + " &",shell=True)

# Now, connect in the same way as always with PyBlueZ
try:
    port=1
    socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    socket.connect((addr,port))
except bluetooth.btcommon.BluetoothError as err:
    # Error handler
    pass
def disconnect():
    #Close socket connection to device
    socket.close()
    
def up():
    #Send 'H' which the Arduino
    #detects as turning the light on
    data = 'w'
    print(data)
    socket.send(data)

def down():
    #Send 'L' to turn off the light
    #attached to the Arduino
    data = 's'
    socket.send(data)
def left():
    #Send 'L' to turn off the light
    #attached to the Arduino
    data = 'a'
    socket.send(data)
def right():
    #Send 'L' to turn off the light
    #attached to the Arduino
    data = 'd'
    socket.send(data)
def clock():
    #Send 'L' to turn off the light
    #attached to the Arduino
    data = 'c'
    socket.send(data)
def anti_clock():
    #Send 'L' to turn off the light
    #attached to the Arduino
    data = 'v'
    socket.send(data)
def nothing():
    data='q'
    socket.send(data)

    
while True:
    key = ord(getch.getch())  
    if key==27:
        disconnect()
        break    
    elif key == 119:
        print('w') 
        up()       
    elif key ==97:
        print('a')
        left()
    elif key ==115:
        print('s')
        down()
    elif key ==100:
        print('d')
        right()
    elif key==99:
        print('c')
        clock()
    elif key==118:
        print('v')
        anti_clock()
    else :
        print('q')
        nothing()

