""" Wireless Sensor Network Simulator 
Designed and Developed by Chinmay R. Gharat """

class PhysicalControlPacket():
    ephy_cntrl_pckt={};
    dphy_cntrl_pckt={};
    def encapsulate_packet(self,pckt):
        self.ephy_cntrl_pckt[0]=pckt;
        return self.ephy_cntrl_pckt;
    def decapsulate_packet(self,pckt):
        self.dphy_cntrl_pckt[0]=pckt[0][0];
        return self.dphy_cntrl_pckt;