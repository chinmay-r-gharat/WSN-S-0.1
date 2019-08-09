""" Wireless Sensor Network Simulator 
Designed and Developed by Chinmay R. Gharat """

""" Scheduler Queue """

import heapq

class Scheduler():
    event_queue=[];
    global_timer=0;
    def schedule_event(self,time,event):
        if (time,event) not in self.event_queue:
            heapq.heappush(self.event_queue,(time,event));
    def run_event(self):
        if len(self.event_queue)==0:
            self.l=0;
            self.t=0;
            self.e=0;
        else:
            self.l=1;
            self.t, self.e=heapq.heappop(self.event_queue);
        return self.t,self.e,self.l;
    def get_time(self):
        return self.global_timer;
    def set_time(self,time):
        self.global_timer=time;