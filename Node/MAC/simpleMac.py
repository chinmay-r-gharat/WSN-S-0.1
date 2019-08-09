""" Wireless Sensor Network Simulator 
Designed and Developed by Chinmay R. Gharat """

from Node import nodeParameters
from Node.MAC import macPacket
from Node.MAC import macControlCommand
from Node.MAC import macControl
class mac_protocol():
    def __init__(self):
        self.m=macPacket.MacPacket();
        self.mc=macControl.MacControl();
    def perform_action(self, action, node, encap_nw_pckt):
        if action=="encapsulate":
            node.npr_mac=self.m.encapsulate_packet(0.01,encap_nw_pckt);
            node.trace_obj.write("-->Node:"+str(node.node_id)+" Encapsulates Packet\n");
            node.trace_obj.write("-->Node:"+str(node.node_id)+" Transfers Packet to Physical layer\n");
            return str(node.node_id)+"-physical"+"_encapsulate", nodeParameters.node_processing_delay;
        elif action=="decapsulate":
            a,decap=self.m.decapsulate_packet(node.npr_phy_d);
            node.npr_mac_d=decap;
            node.npr_phy_d=-1;
            node.trace_obj.write("-->Node:"+str(node.node_id)+" Decapsulates Packet\n");
            node.trace_obj.write("-->Node:"+str(node.node_id)+" Transfers Packet to Network layer\n");
            return str(node.node_id)+"-network"+"_decapsulate", nodeParameters.node_processing_delay;
        elif action=="check.transport.control":
            node.trace_obj.write("-->Node:"+str(node.node_id)+" Transfers Packet to Physical layer\n");
            return str(node.node_id)+"-physical"+"_encapsulate.transport.control", nodeParameters.node_processing_delay;
        elif action=="check.network.control":
            node.trace_obj.write("-->Node:"+str(node.node_id)+" Transfers Packet to Physical layer\n");
            return str(node.node_id)+"-physical"+"_encapsulate.network.control", nodeParameters.node_processing_delay;
        elif action=="encapsulate.control":
            node.npr_mac=self.mc.encapsulate_control_packet(macControlCommand.MacControlCommand.MC1);
            return str(node.node_id)+"-physical"+"_encapsulate.network.control", nodeParameters.node_processing_delay;
        elif action=="decapsulate.control":
            node.npr_mac_d=self.mc.decapsulate_control_packet(node.npr_phy_d);
            return -1,-1;