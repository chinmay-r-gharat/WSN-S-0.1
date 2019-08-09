""" Wireless Sensor Network Simulator 
Designed and Developed by Chinmay R. Gharat """

class ApplicationPacket():
    def __init__(self):
        self.eapp_pckt={};
    def encapsulate_packet(self,raw_data,pid,nid,ts):
        self.eapp_pckt[0]=raw_data;
        self.eapp_pckt[1]=pid;
        self.eapp_pckt[2]=nid;
        self.eapp_pckt[3]=ts;
        return self.eapp_pckt;
    def decapsulate_packet(self,trans_pckt):
        self.raw_data=trans_pckt[0][0];
        self.pid=trans_pckt[0][1];
        self.nid=trans_pckt[0][2];
        self.ts=trans_pckt[0][3];
        return self.raw_data, self.pid, self.nid, self.ts;