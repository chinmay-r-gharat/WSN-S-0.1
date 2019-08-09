""" Wireless Sensor Network Simulator 
Designed and Developed by Chinmay R. Gharat """

class MacControl():
    emac_cntrl_pckt={};
    def encapsulate_control_packet(self,control_packet):
        self.emac_cntrl_pckt[0]=control_packet;
        return self.emac_cntrl_pckt;
    def decapsulate_control_packet(self,control_packet):
        self.dmac_cntrl_pckt=control_packet[0];
        return self.dmac_cntrl_pckt;