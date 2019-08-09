""" Wireless Sensor Network Simulator 
Designed and Developed by Chinmay R. Gharat """

from Node import nodeModeEnum
from Node.Physical import physicalPacket
from Node import nodeParameters
from Node.Physical import physicalControlPacket
class physical_protocol():
    def __init__(self):
        self.p=physicalPacket.PhysicalPacket();
        self.pc=physicalControlPacket.PhysicalControlPacket();
    def perform_action(self, action, node, encap_mac_pckt):
        if action=="encapsulate":
            node.npr_phy=self.p.encapsulate_packet(node.node_id,node.node_rssi,encap_mac_pckt);
            print("Encapsulating: ",node.npr_phy);
            return str(node.node_id)+"-physical"+"_transmit", nodeParameters.node_processing_delay;
        elif action=="transmit":
            print("Transmitting: ",node.npr_phy);
            node.node_mode=nodeModeEnum.node_mode_enum.MODE_TX;
            return str(node.node_id)+"-channel"+"_process", nodeParameters.node_processing_delay;
        elif action=="transmit.control":
            node.node_mode=nodeModeEnum.node_mode_enum.MODE_TX;
            return str(node.node_id)+"-channel"+"_process.control", nodeParameters.node_processing_delay;
        elif action=="transmit.done":
            node.npr_phy={};
            node.node_mode=nodeModeEnum.node_mode_enum.MODE_IDLE;
            if node.node_type.value==1:
                return str(node.node_id)+"-application"+"_sample", node.app_samp_t;
            else:
                return -1,-1;
        elif action=="recieved":
            if node.npr_recieve:
                print(node.npr_recieve)
                n_id,rssi_d,decap=self.p.decapsulate_packet(node.npr_recieve);
                node.trace_obj.write("-->Node:"+str(node.node_id)+" Recieved Packet from:"+str(n_id)+"\n");
                node.npr_phy_d=decap;
                node.node_mode=nodeModeEnum.node_mode_enum.MODE_PROCESSING;
                return str(node.node_id)+"-mac"+"_decapsulate", nodeParameters.node_processing_delay;
            else:
                return -1,-1;
            node.npr_recieve={};
        elif action=="encapsulate.transport.control":
            node.npr_phy=self.pc.encapsulate_packet(node.npr_trans);
            return str(node.node_id)+"-physical"+"_transmit.control", nodeParameters.node_processing_delay;
        elif action=="decapsulate.transport.control":
            node.npr_phy_d=self.pc.decapsulate_packet(node.npr_recieve);
            node.npr_recieve={};
            return str(node.node_id)+"-transport"+"_decapsulate.control", nodeParameters.node_processing_delay;
        elif action=="encapsulate.network.control":
            node.npr_phy=self.pc.encapsulate_packet(node.npr_nw);
            return str(node.node_id)+"-physical"+"_transmit.control", nodeParameters.node_processing_delay;
        elif action=="decapsulate.network.control":
            node.npr_phy_d=self.pc.decapsulate_packet(node.npr_recieve);
            node.npr_recieve={};
            return str(node.node_id)+"-network"+"_decapsulate.control", nodeParameters.node_processing_delay;
        elif action=="encapsulate.mac.control":
            node.npr_phy=self.pc.encapsulate_packet(node.npr_mac);
            return str(node.node_id)+"-physical"+"_transmit.control", nodeParameters.node_processing_delay;
        elif action=="decapsulate.mac.control":
            node.npr_phy_d=self.pc.decapsulate_packet(node.npr_recieve);
            node.npr_recieve={};
            return str(node.node_id)+"-mac"+"_decapsulate.control", nodeParameters.node_processing_delay;