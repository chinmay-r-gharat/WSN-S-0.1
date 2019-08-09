""" Wireless Sensor Network Simulator 
Designed and Developed by Chinmay R. Gharat """

""" interpreter """
from Node import Node
from Node import nodeModeEnum
from Node import nodeTypeEnum
from Node import nodeParameters
from Channel import channelModel
from Scheduler import scheduler
from Process import randomProcess
import simulationScenario 
import sys

""" Creating node objects
creats node with defined topology
allocates node mode and type """
n=[];
source_node=[];      
sink_node=-1;
p=randomProcess.RandomProcess();
s=scheduler.Scheduler();
trace=open("trace-info.txt","w");

""" Event Executer Fucntion """
def event_checker_node(node,layer,event):
    #n[node].node_mode=nodeModeEnum.node_mode_enum.MODE_IDLE;
    eventr,time=n[node].event_processor(event,layer,node,s.get_time());
    return eventr, time;

def event_checker_channel(channel_obj,action,node,x_loc,y_loc):
    eventr,time=channel_obj.event_processor(action,node,x_loc,y_loc);
    return eventr, time;

""" Event Paerser"""
def event_parser(t,e):
    for i in range(len(e)):
        if e[i]=="-":
           fp=i;
        elif e[i]=="_":
            np=i;
    no_num=e[0:fp];
    no_layer=e[fp+1:np];
    no_event=e[np+1:len(e)]; 
    return no_num, no_layer, no_event;
    
if simulationScenario.nn != len(simulationScenario.x_loc) or simulationScenario.nn != len(simulationScenario.y_loc):
    sys.exit("Error NN1, Mismatch between number of nodes and number of locations defined....");
for i in range(simulationScenario.nn) :
    if simulationScenario.n_types[i]=="so" :
        source_node.append(i);
        n_type=nodeTypeEnum.node_type_enum.TYPE_SOURCE;
    elif simulationScenario.n_types[i]=="si" :
        sink_node=i;
        n_type=nodeTypeEnum.node_type_enum.TYPE_SINK;
    elif simulationScenario.n_types[i]=="r" :
        n_type=nodeTypeEnum.node_type_enum.TYPE_RELAY;
    else :
        sys.exit("Error NTD1, Wrong node type defined....");
    n.append(Node.node(i, simulationScenario.x_loc[i], simulationScenario.y_loc[i], nodeModeEnum.node_mode_enum.MODE_IDLE, 
                       n_type,nodeParameters.node_starting_energy,-1,simulationScenario.node_tx_power,trace,-1));

c=channelModel.ChannelModel(simulationScenario.nn,simulationScenario.x_loc,simulationScenario.y_loc,n,s);

""" Updating value of sink node """
for i in range(simulationScenario.nn):
    n[i].sink_id=sink_node;
    
"""Updating sampling Time"""
for i in range(len(source_node)):
    n[source_node[i]].app_samp_t=simulationScenario.app_sr[i];

""" Initialising Sampling Events """   
for i in range(len(source_node)):        
    s.schedule_event(0,str(source_node[i])+"-application_start");
    
""" Initialising End Event """
s.schedule_event(int(simulationScenario.sim_time),"-simmulation_end");
    
""" Event running Loop """
print("Simulating",end='')
trace.write("Starting Simulation \n");
while True:
        if s.get_time() >= simulationScenario.sim_time:
            print("Simulation Completed",end='');
            trace.close();
            break
        else:
            print(".",end='');
            t,e,l=s.run_event();
            if t==int(simulationScenario.sim_time):#new
                l=0;
            if l!=0:   
                print("Event:"+str(e)+" Time:"+str(t));
                no_num, no_layer, no_event=event_parser(t,e);
                print("Node:"+no_num+" mode:"+str(n[int(no_num)].node_mode))
                if n[int(no_num)].node_energy>0:
                    trace.write("Time:"+str(t)+" Node:"+str(no_num)+" Layer:"+str(no_layer)+" Event:"+str(no_event)+"\n");
                if no_layer!="channel":
                    eventr,time=event_checker_node(int(no_num),no_layer,no_event);#changed
                elif no_layer=="channel":
                    eventr,time=event_checker_channel(c,no_event,n[int(no_num)],simulationScenario.x_loc,simulationScenario.y_loc);
                s.set_time(t);
                if eventr!=-1:
                    s.schedule_event(time+s.get_time(),eventr);
            else:
                s.set_time(simulationScenario.sim_time);