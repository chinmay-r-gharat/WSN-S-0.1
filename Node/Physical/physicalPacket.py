""" Wireless Sensor Network Simulator 
Designed and Developed by Chinmay R. Gharat """

class PhysicalPacket():
    def __init__(self):
        self.ephy_pckt={};
        self.dphy_pckt={};
    def encapsulate_packet(self,node_id,RSSI,mac_pckt):
        self.ephy_pckt[0]=node_id;
        self.ephy_pckt[1]=RSSI;
        self.ephy_pckt[2]=mac_pckt;
        return self.ephy_pckt;
    def decapsulate_packet(self,phy_pckt):
        self.node_id=phy_pckt[0];
        self.RSSI=phy_pckt[1];
        self.dphy_pckt[0]=phy_pckt[2];
        return self.node_id, self.RSSI, self.dphy_pckt;