from numpy import *
import matplotlib.pyplot as plt

class BINARY(object):
    def __init__(self, _m1=4*pi*pi, _v10=[0,2.*pi], _dt=0.001, _time=1, _beta = 2):
        self.m1=_m1 
        self.x1, self.y1= [1.0],[0]
        self.vx1, self.vy1= [_v10[0]],[_v10[1]]
        self.dt=_dt
        self.time= _time
        self.n=int(_time/_dt)
        self.beta = _beta 
    def cal(self):
        for i in range(self.n):
            self.r=sqrt((self.x1[-1])**2+(self.y1[-1])**2)
            self.vx1.append(self.vx1[-1]+self.dt*(-self.m1*self.x1[-1]/self.r**(self.beta + 1)))
            self.vy1.append(self.vy1[-1]+self.dt*(-self.m1*self.y1[-1]/self.r**(self.beta + 1)))
            self.x1.append(self.x1[-1]+self.dt*self.vx1[-1])
            self.y1.append(self.y1[-1]+self.dt*self.vy1[-1])
    def plot_trajectory(self,_ax):
        _ax.plot(self.x1,self.y1,'-b')
        _ax.plot([self.x1[-1]],[self.y1[-1]],'ob',markersize=8)
        _ax.plot(0, 0,'or',markersize=16)
        
 
ax1=plt.axes([0.1,0.1,0.7,0.7])
ax1.set_xlabel(r'$x$'+' (AU)',fontsize=18)
ax1.set_ylabel(r'$y$'+' (AU)',fontsize=18)
ax1.set_title('Circular orbits',fontsize=18)

cmp=BINARY()
cmp.cal()
cmp.plot_trajectory(ax1)

plt.show()