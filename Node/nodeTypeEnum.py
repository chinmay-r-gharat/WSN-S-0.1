""" Wireless Sensor Network Simulator 
Designed and Developed by Chinmay R. Gharat """

""" Enumerator Class for defining types of node in WSN 
Three types are defined:Source(TYPE_SOURCE), Sink(TYPE_SINK), Relay(TYPE_RELAY) """
from enum import Enum
class node_type_enum(Enum):
    TYPE_SOURCE=1
    TYPE_SINK=2
    TYPE_RELAY=3