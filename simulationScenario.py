""" Wireless Sensor Network Simulator 
Designed and Developed by Chinmay R. Gharat """

""" Defining Simulation time """
sim_time=1000;
""" Defining number of nodes """
nn=10;
""" Node Transmission Power """
node_tx_power=5;
""" Defning node locations """
x_loc=[1,30,60,90,120,150,180,210,240,270];
y_loc=[1,1,1,1,1,1,1,1,1,1];
""" Defining node types """
n_types=["so","r","r","r","r","r","r","r","r","si"];
""" DEfining the protocols used in layers """
app_lay_proto=["Node.Application.simpleSampler"];
trans_lay_proto=["Node.Transport.simpleTransport"];
ntwrk_lay_proto=["Node.Network.simpleNetwork"];
mac_lay_proto=["Node.MAC.genericCSMA"];
phy_lay_proto=["Node.Physical.simplePhysical"];
""" Defining Application Sampling Rate """
app_sr=[0.5];
