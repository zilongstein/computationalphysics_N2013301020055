import math 
import matplotlib.pyplot as plt

x=[];y=[]
v_x=[];v_y=[]
dt=0.001;r_init=1;theta=0
v_y.append(6.28);v_x.append(0);a=4*math.pi**2
x.append(r_init*math.cos(theta));y.append(r_init*math.sin(theta))
while x[-1] <=1:
    r=math.sqrt(x[-1]**2+y[-1]**2)
    v_x_tmp=v_x[-1]-dt*a*x[-1]*r**(-3)
    v_x.append(v_x_tmp)
    x_tmp=x[-1]+dt*v_x[-1]
    x.append(x_tmp)
    v_y_tmp=v_y[-1]-dt*a*y[-1]*r**(-3)
    v_y.append(v_y_tmp)
    y_tmp=y[-1]+dt*v_y[-1]
    y.append(y_tmp)
    
plt.plot(x,y,'b-')
plt.plot([0],[0],'or',markersize=20)
plt.title('Mercury circular obrit ')
plt.xlabel('x');plt.ylabel('y')
print x[-1]
plt.savefig("y-x.png")
plt.show()
