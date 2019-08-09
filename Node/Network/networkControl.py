""" Wireless Sensor Network Simulator 
Designed and Developed by Chinmay R. Gharat """

class NetworkControl():
    enw_cntrl_pckt={};
    def encapsulate_control_packet(self,control_packet):
        self.enw_cntrl_pckt[0]=control_packet;
        return self.enw_cntrl_pckt;
    def decapsulate_control_packet(self,control_packet):
        self.dnw_cntrl_pckt=control_packet[0];
        return self.dnw_cntrl_pckt;