""" Wireless Sensor Network Simulator 
Designed and Developed by Chinmay R. Gharat """

class TransportPacket():
    def __init__(self):
        self.etrans_pckt={};
        self.dtrans_pckt={};
    def encapsulate_packet(self,dsid,src,dst,app_pckt):
        self.etrans_pckt[0]=dsid;
        self.etrans_pckt[1]=src;
        self.etrans_pckt[2]=dst;
        self.etrans_pckt[3]=app_pckt;
        return self.etrans_pckt;
    def decapsulate_packet(self,ntwrk_pckt):
        self.dsid=ntwrk_pckt[0][0];
        self.src=ntwrk_pckt[0][1];
        self.dst=ntwrk_pckt[0][2];
        self.dtrans_pckt[0]=ntwrk_pckt[0][3];
        return self.dsid, self.src, self.dst, self.dtrans_pckt;