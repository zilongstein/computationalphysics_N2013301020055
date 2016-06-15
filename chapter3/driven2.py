import math
import matplotlib.pyplot as plt

g=9.8
l=1.0
class driven_pendulum():
    def __init__(self,_omg0,_theta0,_dt,_time,_t0,_q,_FD,_Omega):
        self.omg=[_omg0]
        self.theta=[_theta0]
        self.t=[_t0]
        self.time=_time
        self.dt=_dt
        self.n=int(_time/_dt)
        self.q=_q
        self.FD=_FD
        self.Omega=_Omega
    def calculate(self):
        for i in range(self.n):
            self.omg.append(self.omg[-1]-g/l*self.theta[-1]*self.dt-self.q*self.omg[-1]*self.dt+self.FD*math.sin(self.Omega*self.t[-1])*self.dt)
            self.theta.append(self.theta[-1]+self.omg[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
    def plot(self,color,label):
        plt.plot(self.t,self.theta,color,label="$\Omega$=$%.1f$,F=$%.1f$,q=$%.1f$"%(self.Omega,self.FD,self.q))

A=driven_pendulum(0,10*math.pi/180,0.01,20,0,1.0,0.2,1.0)
B=driven_pendulum(0,10*math.pi/180,0.01,20,0,1.0,0.2,2.0)
C=driven_pendulum(0,10*math.pi/180,0.01,20,0,1.0,0.2,3.0)
A.calculate()
B.calculate()
C.calculate()
A.plot('b-',label="$\Omega$=$1.0$,F=$0.1$,q=$1.0$")
B.plot('g-',label="$\Omega$=$2.0$,F=$0.2$,q=$1.0$")
C.plot('r-',label="$\Omega$=$3.0$,F=$0.3$,q=$1.0$")
plt.xlim(0,20)
plt.xlabel("time(s)")
plt.ylabel("$\Theta$(radians)")
plt.title("driven_pendulum")
plt.legend(fontsize=10,loc='best')
plt.savefig("driven_pendulum2.png")

plt.show()
