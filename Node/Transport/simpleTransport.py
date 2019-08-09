""" Wireless Sensor Network Simulator 
Designed and Developed by Chinmay R. Gharat """

from Node import nodeParameters
from Node.Transport import transportPacket
from Node.Transport import transportControlCommand
from Node.Transport import transportControl
class transport_protocol():
    def __init__(self):
        self.t=transportPacket.TransportPacket();
        self.tc=transportControl.TransportControl();
    def perform_action(self, action, node, encap_app_pckt):
        if action=="encapsulate":
            node.npr_trans=self.t.encapsulate_packet(node.sink_id,node.node_id,'dst',node.npr_app);
            node.trace_obj.write("-->Node:"+str(node.node_id)+" Encapsulates Packet\n");
            node.trace_obj.write("-->Node:"+str(node.node_id)+" Transfers Packet to Network layer\n");
            return str(node.node_id)+"-network"+"_encapsulate", nodeParameters.node_processing_delay;
        elif action=="decapsulate":
            a,b,c,decap=self.t.decapsulate_packet(node.npr_nw_d);
            node.npr_trans_d=decap;
            node.npr_nw_d={};
            node.trace_obj.write("-->Node:"+str(node.node_id)+" Decapsulates Packet\n");
            node.trace_obj.write("-->Node:"+str(node.node_id)+" Transfers Packet to Application layer\n");
            return str(node.node_id)+"-application"+"_decapsulate", nodeParameters.node_processing_delay;
        elif action=="encapsulate.control":
            node.npr_trans=self.tc.encapsulate_control_packet(transportControlCommand.TransportControlCommand.TC1);
            return str(node.node_id)+"-mac"+"_check.transport.control", nodeParameters.node_processing_delay;
        elif action=="decapsulate.control":
            node.npr_trans_d=self.tc.decapsulate_control_packet(node.npr_phy_d);
            return -1,-1;