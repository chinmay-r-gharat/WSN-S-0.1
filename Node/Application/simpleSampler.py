""" Wireless Sensor Network Simulator 
Designed and Developed by Chinmay R. Gharat """

from Node import nodeModeEnum
from Node import nodeParameters
from Node.Application import applicationPacket
from Process import randomProcess

class application_protocol():
    def __init__(self):
        self.a=applicationPacket.ApplicationPacket();
        self.p=randomProcess.RandomProcess();
    def sample(self):
        self.s=self.p.sample_value();
        return self.s;
    def perform_action(self, action, no_de, time_stamp):
        if action=="start":
            no_de.node_mode=nodeModeEnum.node_mode_enum.MODE_IDLE;
            return str(no_de.node_id)+"-application"+"_sample", no_de.app_samp_t;
        elif action=="sample":
            sa=self.sample();
            no_de.node_buffer.put(sa);
            no_de.trace_obj.write("-->Node:"+str(no_de.node_id)+" Samples value:"+str(sa)+"\n");
            return str(no_de.node_id)+"-application"+"_encapsulate", nodeParameters.node_processing_delay;
        elif action=="encapsulate":
            if no_de.node_buffer.empty()==False:
                no_de.pid=no_de.pid+1;
                no_de.trace_obj.write("-->Node:"+str(no_de.node_id)+" Encapsulates Packet with PID:"+str(no_de.pid)+"\n");
                no_de.trace_obj.write("-->Node:"+str(no_de.node_id)+" Transfers Packet with PID:"+str(no_de.pid)+" to transport layer"+"\n");
                no_de.npr_app=self.a.encapsulate_packet(no_de.node_buffer.get(),no_de.pid,no_de.node_id,time_stamp);
                print("encapsulating for:",no_de.node_id)
                return str(no_de.node_id)+"-transport"+"_encapsulate", nodeParameters.node_processing_delay;
        elif action=="decapsulate":
            a1,a2,a3,a4=self.a.decapsulate_packet(no_de.npr_trans_d);
            no_de.trace_obj.write("-->Node:"+str(no_de.node_id)+" Decapsulates Packet with conetent:"+str(a1)+"\n");
            no_de.npr_trans_d={};
            no_de.node_mode=nodeModeEnum.node_mode_enum.MODE_IDLE;
            return -1,-1;