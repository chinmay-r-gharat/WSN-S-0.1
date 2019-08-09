""" Wireless Sensor Network Simulator 
Designed and Developed by Chinmay R. Gharat """

class NetworkPacket():
    def __init__(self):
        self.entwrk_pckt={};
        self.dntwrk_pckt={};
    def encapsulate_packet(self,src,dest,nxthp,trans_pckt):
        self.entwrk_pckt[0]=src;
        self.entwrk_pckt[1]=dest;
        self.entwrk_pckt[2]=nxthp;
        self.entwrk_pckt[3]=trans_pckt;
        return self.entwrk_pckt;
    def decapsulate_packet(self,mac_pckt):
        self.src=mac_pckt[0][0];
        self.dest=mac_pckt[0][1];
        self.nxthp=mac_pckt[0][2];
        self.dntwrk_pckt[0]=mac_pckt[0][3];
        return self.src, self.dest, self.nxthp, self.dntwrk_pckt;