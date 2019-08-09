""" Wireless Sensor Network Simulator 
Designed and Developed by Chinmay R. Gharat """

""" calculation of pathloss for each node 
as the nodes are static, pathloss is calculated
only at the recieving end """
import math
import numpy
from Channel import channelParameters
from Node import nodeModeEnum
from Node import nodeParameters

class ChannelModel():
    distance=[]
    Pld=[]
    bd_pathloss=[]
    path_loss=[]
    recieving_nodes=[]
    tx_affected_node=[]
    def __init__(self,nn,x_loc,y_loc,node_obj,sch):
        self.sch=sch;
        self.node_obj=node_obj;
        self.nn=nn;
        self.x=x_loc;
        self.y=y_loc;
    def distance_calculate(self,node_id):
        for i in range(self.nn):
                self.distance.append(math.sqrt((self.x[node_id]-self.x[i])*(self.x[node_id]-self.x[i])+
                                           (self.y[node_id]-self.y[i])*(self.y[node_id]-self.y[i])));
    def pathLoss_calculate(self,node_id):
        for i in range(self.nn):
            temp=self.distance[i];
            if i!=node_id:
                temp1=math.log10(temp/channelParameters.channel_d0);
                temp2=numpy.random.normal(0,channelParameters.channel_sigma);
            elif i==node_id:
                temp1=0;
                temp2=0;
            self.Pld.append(channelParameters.channel_pld0+10*channelParameters.channel_eta*temp1+temp2);
            #self.bd_pathloss.append(numpy.random.normal(0,channelParameters.channel_bdsigma)/2);
            self.bd_pathloss.append(0);
            self.path_loss.append(self.Pld[i]+self.bd_pathloss[i]);
        self.path_loss[node_id]=1000;#Huge path loss just to make sure tx node doesnot recieve its own packet
    def path_loss_calculate(self,node_id,x_loc,y_loc):
        self.distance_calculate(node_id);    
        self.pathLoss_calculate(node_id);
    def clearing_list(self,n):
        if n==1:
            self.distance.clear();
            self.Pld.clear();
            self.bd_pathloss.clear();
            self.path_loss.clear();
        else:    
            self.distance.clear();
            self.Pld.clear();
            self.bd_pathloss.clear();
            self.path_loss.clear();    
            self.recieving_nodes.clear();
            self.tx_affected_node.clear();
    def event_processor(self, action, node, x_loc, y_loc):
        if action=="process" or action=="process.control":
            self.clearing_list(1);
            self.path_loss_calculate(node.node_id, x_loc, y_loc);
            for i in range(len(self.path_loss)):
                print("path loss is:"+str(self.path_loss[i])+" for node:"+str(i))
                if (node.node_tx_power-self.path_loss[i])>=nodeParameters.node_sinr_threshold:
                    self.node_obj[i].node_rssi=node.node_tx_power-self.path_loss[i];
                    self.tx_affected_node.append(i);
                    if  self.node_obj[i].node_mode.value==4:
                        self.recieving_nodes.append(i);
                        self.node_obj[i].node_mode=nodeModeEnum.node_mode_enum.MODE_RX;
                        self.node_obj[i].npr_recieve=node.npr_phy; #this is correct
                        print("Recieved power is"+str(node.node_tx_power-self.path_loss[i]))
                        print("node phy",node.npr_phy)
                        print("tx node:"+str(node.node_id)+" rx node:"+str(i));
            if action=="process":
                return str(node.node_id)+"-channel"+"_done", nodeParameters.node_packet_size/nodeParameters.node_tx_rate;
            elif action=="process.control":
                return str(node.node_id)+"-channel"+"_done.control", nodeParameters.node_packet_size/nodeParameters.node_tx_rate;
        elif action=="done" or action=="done.control":
            for i in range(len(self.recieving_nodes)):
                node.trace_obj.write("-->Node:"+str(self.recieving_nodes[i])+" Recieved Packet from:"+str(node.node_id)+"\n");
                if action=="done":
                    self.sch.schedule_event(nodeParameters.node_processing_delay+self.sch.get_time(),str(self.recieving_nodes[i])+"-physical_recieved");
                elif action=="done.control":
                    self.sch.schedule_event(nodeParameters.node_processing_delay+self.sch.get_time(),str(self.recieving_nodes[i])+"-physical_decapsulate.transport.control");                    
            for i in range(len(self.tx_affected_node)):
                self.node_obj[self.tx_affected_node[i]].node_rssi=-1111;
            self.clearing_list(2);
            return str(node.node_id)+"-physical"+"_transmit.done", 0;