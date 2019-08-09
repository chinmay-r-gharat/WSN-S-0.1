""" Wireless Sensor Network Simulator 
Designed and Developed by Chinmay R. Gharat """

""" Enumerator Class for defining modes of node in WSN 
Four modes are defined:Transmitter Mode(MODE_TX), Reciever Mode(MODE_RX),
Idle Mode(MODE_IDLE) and Sleep Mode(MODE_SLEEP) """
from enum import Enum
class node_mode_enum(Enum):
    MODE_TX=1
    MODE_RX=2
    MODE_PROCESSING=3
    MODE_IDLE=4
    MODE_SLEEP=5
    MODE_DEAD=6