from pylab import *
import math

sigma = 10
b = 8./3
r = 25

class state:
    def __init__(self, _x, _y, _z, _t):
        self.x = _x
        self.y = _y
        self.z = _z
        self.t = _t
        
class lorenz:
    def __init__(self, _s = state( 0, 0, 0, 0), _dt = 0):
        self.lorenz_state = []
        self.lorenz_state.append(_s)
        self.dt = _dt
        
    def next_state(self,current_state):
        global r,b,sigma
        next_x = current_state.x + sigma * (current_state.y - current_state.x) * self.dt
        next_y = current_state.y + ( - current_state.x * current_state.z + r * current_state.x - current_state.y) * self.dt
        next_z = current_state.z + (current_state.x * current_state.y - b * current_state.z) * self.dt
        return state( next_x, next_y, next_z, current_state.t + self.dt)
        
    def move(self):
        while not (self.lorenz_state[-1].t > 500):
            self.lorenz_state.append(self.next_state(self.lorenz_state[-1]))
            
    def trajectory(self):
        x = []
        y = []
        z = []
        t = []
        for s in self.lorenz_state:
            x.append(s.x)
            y.append(s.y)
            z.append(s.z)
            t.append(s.t)
        x0 = []
        y0 = []
        z0 = []
        z00 = []
        i = 0
        while i < len(x):
            if abs(x[i]) <= 0.01:
                y0.append(y[i])
                z0.append(z[i])
            else:
                pass
            if abs(y[i]) <= 0.01:
                x0.append(x[i])
                z00.append(z[i])
            else:
                pass
            i = i + 1
        ax1 = subplot(121)
        ax2 = subplot(122)
        sca(ax1)
        scatter(y0,z0,s = 1)
        xlabel('y')
        ylabel('z')
        sca(ax2)
        scatter(x0,z00,s=1)
        xlabel('x')
        ylabel('z')
        
a = lorenz(state( 1.0, 0, 0, 0), _dt = 0.001)
a.move()
a.trajectory()
show()