import math
import matplotlib.pyplot as plt

g=9.8
l=1
class simple_harmonic():
    def __init__(self,_omg0,_theta0,_dt,_time,_t0):
        self.omg=[_omg0]
        self.theta=[_theta0]
        self.t=[_t0]
        self.time=_time
        self.dt=_dt
        self.n=int(_time/_dt)
    def calculate(self):
        for i in range(self.n):
            self.omg.append(self.omg[-1]-g/l*self.theta[-1]*self.dt)
            self.theta.append(self.theta[-1]+self.omg[-2]*self.dt)
            self.t.append(self.t[-1]+self.dt)
    def plot(self):
        plt.plot(self.t,self.theta,'r-',label="Euler method")
class cromer(simple_harmonic):
    def calculate(self):
        for i in range(self.n):
            self.omg.append(self.omg[-1]-g/l*self.theta[-1]*self.dt)
            self.theta.append(self.theta[-1]+self.omg[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
    def plot(self):
        plt.plot(self.t,self.theta,'b-',label="Euler-Cromer method")
a=simple_harmonic(0,10*math.pi/180,0.0001,20,0)
a.calculate()
a.plot()
b=cromer(0,10*math.pi/180,0.0001,20,0)
b.calculate()
b.plot()
plt.xlabel("time(s)")
plt.ylabel("$\Theta$(radians)")
plt.xlim(0,20)
plt.legend(loc="upper left")
plt.savefig("simple_pendulum.png")
plt.show()