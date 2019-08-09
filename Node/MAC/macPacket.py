""" Wireless Sensor Network Simulator 
Designed and Developed by Chinmay R. Gharat """

class MacPacket():
    def __init__(self):
        self.emac_pckt={};
        self.dmac_pckt={};
    def encapsulate_packet(self,bckt,ntwrk_pckt):#bckt is back-off time
        self.emac_pckt[0]=bckt;
        self.emac_pckt[1]=ntwrk_pckt;
        return self.emac_pckt;
    def decapsulate_packet(self,phy_pckt):
        self.bckt=phy_pckt[0][0];
        self.dmac_pckt[0]=phy_pckt[0][1];
        return self.bckt, self.dmac_pckt;