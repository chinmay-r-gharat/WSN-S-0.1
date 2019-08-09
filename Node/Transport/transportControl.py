""" Wireless Sensor Network Simulator 
Designed and Developed by Chinmay R. Gharat """

class TransportControl():
    etrans_cntrl_pckt={};
    def encapsulate_control_packet(self,control_packet):
        self.etrans_cntrl_pckt[0]=control_packet;
        return self.etrans_cntrl_pckt;
    def decapsulate_control_packet(self,control_packet):
        self.dtrans_cntrl_pckt=control_packet[0];
        return self.dtrans_cntrl_pckt;