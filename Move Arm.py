
import RoboticArmEdgeMovement

# Get Device
dev = RoboticArmEdgeMovement.RoboticArmDevice()

# was it found?
if dev is None:
    raise ValueError('Device not found')

#Start Moving

RoboticArmEdgeMovement.ArmGripperOpen(dev, 0.6)
RoboticArmEdgeMovement.ArmLightOn(dev, 1)
RoboticArmEdgeMovement.ArmGripperClose(dev, 0.6)
RoboticArmEdgeMovement.ArmLightOff(dev, 0)

RoboticArmEdgeMovement.ArmWristDown(dev, 1)
RoboticArmEdgeMovement.ArmWristUp(dev, 1)

RoboticArmEdgeMovement.ArmElbowDown(dev, 1)
RoboticArmEdgeMovement.ArmElbowUp(dev, 1)

RoboticArmEdgeMovement.ArmShoulderDown(dev, 1)
RoboticArmEdgeMovement.ArmShoulderUp(dev, 1)

RoboticArmEdgeMovement.ArmBaseRight(dev, 1)
RoboticArmEdgeMovement.ArmBaseLeft(dev, 1)

RoboticArmEdgeMovement.ArmStop(dev, 0.2)
