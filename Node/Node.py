""" Wireless Sensor Network Simulator 
Designed and Developed by Chinmay R. Gharat """

import importlib
import simulationScenario 
import queue
from Node import nodeModeEnum
from Node import nodeParameters

appPro=simulationScenario.app_lay_proto[0];
a_p=importlib.import_module(appPro);
transPro=simulationScenario.trans_lay_proto[0];
t_p=importlib.import_module(transPro);
nwPro=simulationScenario.ntwrk_lay_proto[0];
n_p=importlib.import_module(nwPro);
macPro=simulationScenario.mac_lay_proto[0];
m_p=importlib.import_module(macPro);
phyPro=simulationScenario.phy_lay_proto[0];
p_p=importlib.import_module(phyPro);
class node():
    prevTime=0;
    timeDiff=0;
    """ Initialising parameters of nodes """
    def __init__(self, node_id, node_pos_x, node_pos_y, node_mode, node_type, node_energy, sink_node_id, tx_power,trace_obj,app_samp_t):
        self.node_id=node_id;
        self.node_pos_x=node_pos_x;
        self.node_pos_y=node_pos_y;
        self.node_mode=node_mode;
        self.node_type=node_type;
        self.node_buffer=queue.Queue(100);
        self.npr_app={};
        self.npr_trans={};
        self.npr_nw={};
        self.npr_mac={};
        self.npr_phy={};
        self.npr_app_d={};
        self.npr_trans_d={};
        self.npr_nw_d={};
        self.npr_mac_d={};
        self.npr_phy_d={};
        self.npr_recieve={};
        self.node_energy=node_energy;
        self.node_rssi=-1111;
        self.sink_id=sink_node_id;
        self.node_tx_power=tx_power;
        self.trace_obj=trace_obj;
        self.pid=0;
        self.app_samp_t=app_samp_t;
        self.ss=a_p.application_protocol();
        self.tt=t_p.transport_protocol();
        self.nn=n_p.network_protocol();
        self.mm=m_p.mac_protocol();
        self.pp=p_p.physical_protocol();
    def event_processor(self, action, layer, node, time_stamp):
        self.timeDiff=time_stamp-self.prevTime;
        self.prevTime=time_stamp;
        if action=="sample" and self.node_mode.value!=4 and self.node_mode.value!=3:
            print("Node Busy sampling cancled: "+str(self.node_mode.value))
            return -1,-1
        if self.node_mode.value==3 and self.node_energy>0.1:#rectify this logic
            self.node_mode=nodeModeEnum.node_mode_enum.MODE_PROCESSING;
            if layer=="application":
                e,t=self.ss.perform_action(action, self, time_stamp);
                self.node_energy=self.node_energy-(nodeParameters.node_processing_delay*nodeParameters.node_processing_watts);
                return e,t;
            elif layer=="transport":
                e,t=self.tt.perform_action(action, self, self.npr_app);
                self.npr_app={};
                self.node_energy=self.node_energy-(nodeParameters.node_processing_delay*nodeParameters.node_processing_watts);
                return e,t;
            elif layer=="network":
                e,t=self.nn.perform_action(action, self, self.npr_trans);
                self.npr_trans={};
                self.node_energy=self.node_energy-(nodeParameters.node_processing_delay*nodeParameters.node_processing_watts);
                return e,t;
            elif layer=="mac":
                e,t=self.mm.perform_action(action, self, self.npr_nw);
                self.npr_nw={};
                self.node_energy=self.node_energy-(nodeParameters.node_processing_delay*nodeParameters.node_processing_watts);
                return e,t;
            elif layer=="physical":
                e,t=self.pp.perform_action(action, self, self.npr_mac);
                self.npr_mac={};
                if action=="encapsulate":
                    self.node_energy=self.node_energy-(nodeParameters.node_processing_delay*nodeParameters.node_processing_watts);
                elif action=="recieved":
                    self.node_energy=self.node_energy-(nodeParameters.node_processing_delay*nodeParameters.node_processing_watts);
                    self.node_energy=self.node_energy-((nodeParameters.node_packet_size/nodeParameters.node_tx_rate)*nodeParameters.node_rx_watts);
                return e,t;
        elif self.node_mode.value==1 and self.node_energy>0.1:
            if layer=="physical":
                e,t=self.pp.perform_action(action, self, self.npr_mac);
                print("node:"+str(self.node_id)+" calling perform_action for node:"+str(node))
                if action=="transmit.done":
                    self.node_energy=self.node_energy-(nodeParameters.node_processing_delay*nodeParameters.node_processing_watts);
                    self.node_energy=self.node_energy-((nodeParameters.node_packet_size/nodeParameters.node_tx_rate)*nodeParameters.node_tx_watts[10]);
                return e,t;
        elif self.node_mode.value==4 and self.node_energy>0.1:
            if layer=="application" and action=="start":
                e,t=self.ss.perform_action(action, self, time_stamp);
                self.node_mode=nodeModeEnum.node_mode_enum.MODE_PROCESSING;
                self.node_energy=self.node_energy-(self.prevTime*nodeParameters.node_idle_watts);
                return e,t;
            elif layer=="application" and action=="sample":
                e,t=self.ss.perform_action(action, self, time_stamp);
                self.node_mode=nodeModeEnum.node_mode_enum.MODE_PROCESSING;
                #self.prevTime=self.prevTime-nodeParameters.node_processing_delay;#check this logic
                self.node_energy=self.node_energy-(self.prevTime*nodeParameters.node_idle_watts);
                return e,t;
            elif layer=="physical" and action=="recieved":#may be not required
                e,t=self.pp.perform_action(action, self, self.npr_mac);
                self.node_mode=nodeModeEnum.node_mode_enum.MODE_PROCESSING;
                self.node_energy=self.node_energy-(self.prevTime*nodeParameters.node_idle_watts);
                return e,t;
        elif self.node_mode.value==2 and self.node_energy>0.1:
            if layer=="physical" and action=="recieved":
                e,t=self.pp.perform_action(action, self, self.npr_mac);
                self.node_energy=self.node_energy-(nodeParameters.node_processing_delay*nodeParameters.node_processing_watts);
                self.node_energy=self.node_energy-((nodeParameters.node_packet_size/nodeParameters.node_tx_rate)*nodeParameters.node_rx_watts);
                return e,t;
        else:
            if self.node_energy<=0:
                self.node_energy=0;
                if self.node_mode.value!=6:
                    self.trace_obj.write("node:"+str(self.node_id)+" out of Energy\n");
                self.node_mode=nodeModeEnum.node_mode_enum.MODE_DEAD;
                return -1,-1;
            return False;