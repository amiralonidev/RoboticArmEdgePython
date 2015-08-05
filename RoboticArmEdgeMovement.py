#in order for this project to work:
#install pyusb: https://github.com/walac/pyusb
#For windows install libusb: http://sourceforge.net/projects/libusb-win32/files/libusb-win32-releases/1.2.6.0/

import usb
import time

# Robotic Arm Edge functions

#Get USB Device
def RoboticArmDevice():
    dev = usb.core.find(idVendor=0x1267, idProduct=0x0000)
    dev.set_configuration()
    return dev;


#Stop
def ArmStop( device, sleeptime ):
    commands = [0,0,0]
    cmd = bytearray(commands)
    ret = device.ctrl_transfer(0x40, 6, 0x100, 0, cmd)
    time.sleep(sleeptime)
    return ret;

#Light On
def ArmLightOn( device, sleeptime ):
    commands = [0,0,1]
    cmd = bytearray(commands)
    ret = device.ctrl_transfer(0x40, 6, 0x100, 0, cmd)
    time.sleep(sleeptime)
    return ret;

#Light off
def ArmLightOff( device, sleeptime ):
    commands = [0,0,0]
    cmd = bytearray(commands)
    ret = device.ctrl_transfer(0x40, 6, 0x100, 0, cmd)
    time.sleep(sleeptime)
    return ret;

#Gripper open
def ArmGripperOpen( device, sleeptime ):
    commands = [2,0,0]
    cmd = bytearray(commands)
    ret = device.ctrl_transfer(0x40, 6, 0x100, 0, cmd)
    time.sleep(sleeptime)
    return ret;

#Gripper close
def ArmGripperClose( device, sleeptime ):
    commands = [1,0,0]
    cmd = bytearray(commands)
    ret = device.ctrl_transfer(0x40, 6, 0x100, 0, cmd)
    time.sleep(sleeptime)
    return ret;

#wrist up
def ArmWristUp( device, sleeptime ):
    commands = [4,0,0]
    cmd = bytearray(commands)
    ret = device.ctrl_transfer(0x40, 6, 0x100, 0, cmd)
    time.sleep(sleeptime)
    return ret;

#wrist Down
def ArmWristDown( device, sleeptime ):
    commands = [0x8,0,0]
    cmd = bytearray(commands)
    ret = device.ctrl_transfer(0x40, 6, 0x100, 0, cmd)
    time.sleep(sleeptime)
    return ret;

#Elbow up
def ArmElbowUp( device, sleeptime ):
    commands = [0x10,0,0]
    cmd = bytearray(commands)
    ret = device.ctrl_transfer(0x40, 6, 0x100, 0, cmd)
    time.sleep(sleeptime)
    return ret;

#Elbow Down
def ArmElbowDown( device, sleeptime ):
    commands = [0x20,0,0]
    cmd = bytearray(commands)
    ret = device.ctrl_transfer(0x40, 6, 0x100, 0, cmd)
    time.sleep(sleeptime)
    return ret;

#Shoulder up
def ArmShoulderUp( device, sleeptime ):
    commands = [0x40,0,0]
    cmd = bytearray(commands)
    ret = device.ctrl_transfer(0x40, 6, 0x100, 0, cmd)
    time.sleep(sleeptime)
    return ret;

#Shoulder Down
def ArmShoulderDown( device, sleeptime ):
    commands = [0x80,0,0]
    cmd = bytearray(commands)
    ret = device.ctrl_transfer(0x40, 6, 0x100, 0, cmd)
    time.sleep(sleeptime)
    return ret;

#Base Right
def ArmBaseRight( device, sleeptime ):
    commands = [0,1,0]
    cmd = bytearray(commands)
    ret = device.ctrl_transfer(0x40, 6, 0x100, 0, cmd)
    time.sleep(sleeptime)
    return ret;

#Base Left
def ArmBaseLeft( device, sleeptime ):
    commands = [0,2,0]
    cmd = bytearray(commands)
    ret = device.ctrl_transfer(0x40, 6, 0x100, 0, cmd)
    time.sleep(sleeptime)
    return ret;
