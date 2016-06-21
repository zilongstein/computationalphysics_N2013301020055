from numpy import *
import matplotlib.pyplot as plt

class BINARY(object):
    def __init__(self, _m1=4*pi*pi, _me=3.*10**(-6), _mj=9.5*10**(-1), _ve0=[0,2.*pi], _vj0=[0,0.88*pi], _dt=0.0001, _time=13):
        self.m1=_m1 
        self.me=_me
        self.mj=_mj
        self.x1, self.y1= [1.],[0]
        self.vx1, self.vy1= [_ve0[0]],[_ve0[1]]
        self.x2, self.y2= [5.2],[0]
        self.vx2, self.vy2=[_vj0[0]], [_vj0[1]]
        self.dt=_dt
        self.time= _time
        self.n=int(_time/_dt)
    def cal(self):
        for i in range(self.n):
            self.re=sqrt(self.x1[-1]**2+self.y1[-1]**2)
            self.rj=sqrt(self.x2[-1]**2+self.y2[-1]**2)
            self.rej=sqrt((self.x1[-1]-self.x2[-1])**2+(self.y1[-1]-self.y2[-1])**2)
            self.vx1.append(self.vx1[-1]+self.dt*(-self.m1*self.x1[-1]/self.re**3-self.m1*self.mj*(self.x1[-1]-self.x2[-1])/self.rej**3))
            self.vy1.append(self.vy1[-1]+self.dt*(-self.m1*self.y1[-1]/self.re**3-self.m1*self.mj*(self.y1[-1]-self.y2[-1])/self.rej**3))
            self.vx2.append(self.vx2[-1]+self.dt*(-self.m1*self.x2[-1]/self.rj**3-self.m1*self.me*(self.x2[-1]-self.x1[-1])/self.rej**3))
            self.vy2.append(self.vy2[-1]+self.dt*(-self.m1*self.y2[-1]/self.rj**3-self.m1*self.me*(self.y2[-1]-self.y1[-1])/self.rej**3))
            self.x1.append(self.x1[-1]+self.dt*self.vx1[-1])
            self.y1.append(self.y1[-1]+self.dt*self.vy1[-1])
            self.x2.append(self.x2[-1]+self.dt*self.vx2[-1])
            self.y2.append(self.y2[-1]+self.dt*self.vy2[-1])
    def plot_trajectory(self,_ax):
        _ax.plot(self.x1,self.y1,'-b')
        _ax.plot(self.x2,self.y2,'-g')
        _ax.plot([self.x1[-1]],[self.y1[-1]],'ob',markersize=8)
        _ax.plot([self.x2[-1]],[self.y2[-1]],'og',markersize=10)
        _ax.plot(0,0,'or',markersize=15)
        
 
ax1=plt.axes([0.1,0.1,0.7,1.0])
ax1.set_xlabel(r'$x$'+' (AU)',fontsize=18)
ax1.set_ylabel(r'$y$'+' (AU)',fontsize=18)
ax1.set_title('three body orbits',fontsize=18)
ax1.text(-5.9,5.3,'$M_J=1000M_J$',fontsize=18)


cmp=BINARY()
cmp.cal()
cmp.plot_trajectory(ax1)

plt.show()