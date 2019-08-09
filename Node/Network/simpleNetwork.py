""" Wireless Sensor Network Simulator 
Designed and Developed by Chinmay R. Gharat """

from Node import nodeParameters
from Node.Network import networkPacket
from Node.Network import networkControlCommand
from Node.Network import networkControl
class network_protocol():
    def __init__(self):
        self.n=networkPacket.NetworkPacket();
        self.nc=networkControl.NetworkControl();
    def perform_action(self, action, node, encap_trans_pckt):
        if action=="encapsulate":
            node.npr_nw=self.n.encapsulate_packet(node.node_id,node.sink_id,"nh",encap_trans_pckt);
            node.trace_obj.write("-->Node:"+str(node.node_id)+" Encapsulates Packet\n");
            node.trace_obj.write("-->Node:"+str(node.node_id)+" Transfers Packet to MAC layer\n");
            return str(node.node_id)+"-mac"+"_encapsulate", nodeParameters.node_processing_delay;
        elif action=="decapsulate":
            a,b,c,decap=self.n.decapsulate_packet(node.npr_mac_d);
            node.npr_nw_d=decap;
            node.npr_mac_d={};
            node.trace_obj.write("-->Node:"+str(node.node_id)+" Decapsulates Packet\n");
            node.trace_obj.write("-->Node:"+str(node.node_id)+" Transfers Packet to Transport layer\n");
            return str(node.node_id)+"-transport"+"_decapsulate", nodeParameters.node_processing_delay;
        elif action=="encapsulate.control":
            node.npr_nw=self.nc.encapsulate_control_packet(networkControlCommand.NetworkControlCommand.NC1);
            return str(node.node_id)+"-mac"+"_check.network.control", nodeParameters.node_processing_delay;
        elif action=="decapsulate.control":
            node.npr_nw_d=self.nc.decapsulate_control_packet(node.npr_phy_d);
            return -1,-1;