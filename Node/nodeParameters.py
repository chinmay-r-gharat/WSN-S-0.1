""" Wireless Sensor Network Simulator 
Designed and Developed by Chinmay R. Gharat """

""" Node Parameters file defines node energy
at various modes of operations, modulation type,
node transmission rate, node SNR Threshold etc."""

node_tx_db=[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5];#differente discrete energy levels
node_tx_watts=[100*10**-3, 120*10**-3, 130*10**-3, 140*10**-3, 150*10**-3, 160*10**-3, 170*10**-3, 180*10**-3, 190*10**-3
               , 200*10**-3, 210*10**-3];#Energy consumed per second by node while transmitting for various discrete energy levels 
node_rx_watts=20*10**-3;#Energy consumed per second by node when recieving 
node_processing_watts=50*10**-3;#Energy consumed per second by node when processing
node_idle_watts=2*10**-3;#Energy consumed per second by node when it is doing nothing
node_tx_rate=1000;#Transmission rate of module in bits per second
node_packet_size=100;#Size of packet in bits
node_sinr_threshold=-95;#Signal to interference noise ratio in dBM
node_processing_delay=0.01;#Delay in seocnds required to process the packet recieved
node_starting_energy=3600;#Starting enegy of node in joules, it is equal to 2400 mAh li-ion battery
node_modulation="ASK";#digital modulation of data