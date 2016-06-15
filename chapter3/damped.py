# -*- coding: utf-8 -*-
"""
Created on Tue Jun 07 08:58:22 2016

@author: asus
"""

import math
import matplotlib.pyplot as plt

g=9.8
l=1
class damped_pendulum():
    def __init__(self,_omg0,_theta0,_dt,_time,_t0,_q):
        self.omg=[_omg0]
        self.theta=[_theta0]
        self.t=[_t0]
        self.time=_time
        self.dt=_dt
        self.n=int(_time/_dt)
        self.q=_q
    def calculate(self):
        for i in range(self.n):
            self.omg.append(self.omg[-1]-g/l*self.theta[-1]*self.dt-self.q*self.omg[-1]*self.dt)
            self.theta.append(self.theta[-1]+self.omg[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
    def plot(self,color,label):
        plt.plot(self.t,self.theta,color,label="q=$%.1f$"%(self.q))
        plt.title("damped_pendulum")
a=damped_pendulum(0,10*math.pi/180,0.01,20,0,10)
b=damped_pendulum(0,10*math.pi/180,0.01,20,0,5)
c=damped_pendulum(0,10*math.pi/180,0.01,20,0,1.0)
a.calculate()
b.calculate()
c.calculate()
a.plot('r-',label='q=$10$')
b.plot('g-',label='q=$5$')
c.plot('b-',label='q=$1.0$')
plt.xlabel("time(s)")
plt.ylabel("$\Theta$(radians)")
plt.xlim(0,20)
plt.legend()
plt.savefig("damped_pendulum.png")
plt.show()