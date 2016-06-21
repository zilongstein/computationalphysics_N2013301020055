from numpy import *
import matplotlib.pyplot as plt

class BINARY(object):
    def __init__(self, _m1=4.4*pi*pi, _m2=4*pi*pi, _v10=[0,2./21.*pi*sqrt(210.)], _v20=[0,-2.2/21.*pi*sqrt(210.)], _dt=0.0001, _time=5):
        self.m1=_m1 
        self.m2=_m2
        self.x1, self.y1= [0.5],[0]
        self.vx1, self.vy1= [_v10[0]],[_v10[1]]
        self.x2, self.y2= [-0.5],[0]
        self.vx2, self.vy2=[_v20[0]], [_v20[1]]
        self.dt=_dt
        self.time= _time
        self.n=int(_time/_dt)
    def cal(self):
        for i in range(self.n):
            self.r=sqrt((self.x1[-1]-self.x2[-1])**2+(self.y1[-1]-self.y2[-1])**2)
            self.vx1.append(self.vx1[-1]+self.dt*(-self.m2*(self.x1[-1]-self.x2[-1])/self.r**3))
            self.vy1.append(self.vy1[-1]+self.dt*(-self.m2*(self.y1[-1]-self.y2[-1])/self.r**3))
            self.vx2.append(self.vx2[-1]+self.dt*(-self.m1*(self.x2[-1]-self.x1[-1])/self.r**3))
            self.vy2.append(self.vy2[-1]+self.dt*(-self.m1*(self.y2[-1]-self.y1[-1])/self.r**3))
            self.x1.append(self.x1[-1]+self.dt*self.vx1[-1])
            self.y1.append(self.y1[-1]+self.dt*self.vy1[-1])
            self.x2.append(self.x2[-1]+self.dt*self.vx2[-1])
            self.y2.append(self.y2[-1]+self.dt*self.vy2[-1])
    def plot_trajectory(self,_ax):
        _ax.plot(self.x1,self.y1,'-b')
        _ax.plot(self.x2,self.y2,'-r')
        _ax.plot([self.x1[-1]],[self.y1[-1]],'ob',markersize=8)
        _ax.plot([self.x2[-1]],[self.y2[-1]],'or',markersize=8)
        
 
ax1=plt.axes([0.1,0.1,0.7,0.7])
ax1.set_xlim(-1.0,1.0)
ax1.set_ylim(-0.8,1.0)
ax1.set_xlabel(r'$x$'+' (AU)',fontsize=18)
ax1.set_ylabel(r'$y$'+' (AU)',fontsize=18)
ax1.set_title('Circular orbits',fontsize=18)
ax1.text(-0.9,0.8,'$M_1/M_2=1.1$',fontsize=18)

cmp=BINARY()
cmp.cal()
cmp.plot_trajectory(ax1)

plt.show()