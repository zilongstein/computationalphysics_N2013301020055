from numpy import *
import matplotlib.pyplot as plt

class BINARY():
    def __init__(self, _e=0.2, _m1=4*pi*pi, _mm=1.2*10**(-7), _mv=2.45*10**(-6), _me=3.*10**(-6), _mj=9.5*10**(-4), _ms=2.85*10**(-4), _vm0=[0,3.65*pi], _vv0=[0,2.34*pi], _ve0=[0,2.*pi], _vj0=[0,0.88*pi], _vs0=[0,0.64*pi], _dt=0.0001, _time=5):
        self.e=_e
        self.m1=_m1
        self.mm=_mm
        self.mv=_mv
        self.me=_me
        self.mj=_mj
        self.ms=_ms
        self.xm, self.ym= [0.30],[0]
        self.vxm, self.vym= [_vm0[0]],[_vm0[1]*sqrt(1+self.e)]
        self.xv, self.yv= [0.72],[0]
        self.vxv, self.vyv= [_vv0[0]],[_vv0[1]]        
        self.xe, self.ye= [1.0],[0]
        self.vxe, self.vye= [_ve0[0]],[_ve0[1]]
        self.xj, self.yj= [5.2],[0]
        self.vxj, self.vyj=[_vj0[0]], [_vj0[1]]
        self.xs, self.ys= [9.54],[0]
        self.vxs, self.vys= [_vs0[0]],[_vs0[1]]
        self.dt=_dt
        self.time= _time
        self.n=int(_time/_dt)
    def cal(self):
        for i in range(self.n):
            self.rm=sqrt(self.xm[-1]**2+self.ym[-1]**2)
            self.rv=sqrt(self.xv[-1]**2+self.yv[-1]**2)
            self.re=sqrt(self.xe[-1]**2+self.ye[-1]**2)
            self.rj=sqrt(self.xj[-1]**2+self.yj[-1]**2)
            self.rs=sqrt(self.xs[-1]**2+self.ys[-1]**2)
            self.rmv=sqrt((self.xm[-1]-self.xv[-1])**2+(self.ym[-1]-self.yv[-1])**2)
            self.rme=sqrt((self.xm[-1]-self.xe[-1])**2+(self.ym[-1]-self.ye[-1])**2)
            self.rmj=sqrt((self.xm[-1]-self.xj[-1])**2+(self.ym[-1]-self.yj[-1])**2)
            self.rms=sqrt((self.xm[-1]-self.xs[-1])**2+(self.ym[-1]-self.ys[-1])**2)
            self.vxm.append(self.vxm[-1]+self.dt*(-self.m1*self.xm[-1]/self.rm**3-self.m1*self.mv*(self.xm[-1]-self.xv[-1])/self.rmv**3-self.m1*self.me*(self.xm[-1]-self.xe[-1])/self.rme**3-self.m1*self.mj*(self.xm[-1]-self.xj[-1])/self.rmj**3-self.m1*self.ms*(self.xm[-1]-self.xs[-1])/self.rms**3))
            self.vym.append(self.vym[-1]+self.dt*(-self.m1*self.ym[-1]/self.rm**3-self.m1*self.mv*(self.ym[-1]-self.yv[-1])/self.rmv**3-self.m1*self.me*(self.ym[-1]-self.ye[-1])/self.rme**3-self.m1*self.mj*(self.ym[-1]-self.yj[-1])/self.rmj**3-self.m1*self.ms*(self.ym[-1]-self.ys[-1])/self.rms**3))
            self.vxv.append(self.vxv[-1]+self.dt*(-self.m1*self.xv[-1]/self.rv**3))
            self.vyv.append(self.vyv[-1]+self.dt*(-self.m1*self.yv[-1]/self.rv**3))
            self.vxe.append(self.vxe[-1]+self.dt*(-self.m1*self.xe[-1]/self.re**3))
            self.vye.append(self.vye[-1]+self.dt*(-self.m1*self.ye[-1]/self.re**3))
            self.vxj.append(self.vxj[-1]+self.dt*(-self.m1*self.xj[-1]/self.rj**3))
            self.vyj.append(self.vyj[-1]+self.dt*(-self.m1*self.yj[-1]/self.rj**3))
            self.vxs.append(self.vxs[-1]+self.dt*(-self.m1*self.xs[-1]/self.rs**3))
            self.vys.append(self.vys[-1]+self.dt*(-self.m1*self.ys[-1]/self.rs**3))
            self.xm.append(self.xm[-1]+self.dt*self.vxm[-1])
            self.ym.append(self.ym[-1]+self.dt*self.vym[-1])
            self.xv.append(self.xv[-1]+self.dt*self.vxv[-1])
            self.yv.append(self.yv[-1]+self.dt*self.vyv[-1])
            self.xe.append(self.xe[-1]+self.dt*self.vxe[-1])
            self.ye.append(self.ye[-1]+self.dt*self.vye[-1])
            self.xj.append(self.xj[-1]+self.dt*self.vxj[-1])
            self.yj.append(self.yj[-1]+self.dt*self.vyj[-1])
            self.xs.append(self.xs[-1]+self.dt*self.vxs[-1])
            self.ys.append(self.ys[-1]+self.dt*self.vys[-1])
    def plot_trajectory(self,_ax):
        _ax.plot(self.xm,self.ym,'-b')
        _ax.plot([self.xm[-1]],[self.ym[-1]],'ob',markersize=2)
        _ax.plot(0,0,'or',markersize=7)
        
 
ax1=plt.axes([0.1,0.1,0.7,1.0])
ax1.set_xlim(0.2995,0.3001)
ax1.set_ylim(-0.0003,0.0003)
ax1.set_xlabel(r'$x$'+' (AU)',fontsize=18)
ax1.set_ylabel(r'$y$'+' (AU)',fontsize=18)
ax1.set_title('Mercury orbit precession',fontsize=18)

cmp=BINARY()
cmp.cal()
cmp.plot_trajectory(ax1)

plt.show()