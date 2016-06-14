import math 
import matplotlib.pyplot as plt

x=[];y=[];z=[]
v_x=[];v_y=[];v_z=[]
dt=0.001;g=-9.8;v_init=45;Sm=4*10**(-4);Bm=-4*10**(-3);w=259.44;theta=0.6
x.append(0.0);y.append(1.8);z.append(0.0)
v_x.append(v_init*math.cos(theta));v_y.append(v_init*math.sin(theta));v_z.append(0.0)
while y[-1]>=0.0:
    v=math.sqrt(v_x[-1]**2+v_y[-1]**2+v_z[-1]**2)
    x_tmp=x[-1]+dt*v_x[-1]
    x.append(x_tmp)
    v_x_tmp=v_x[-1]+dt*Bm*v*v_x[-1]
    y_tmp=y[-1]+dt*v_y[-1]
    y.append(y_tmp)
    v_y_tmp=v_y[-1]+dt*g+dt*Sm*w*v_x[-1]+dt*Bm*v*v_y[-1]
    v_y.append(v_y_tmp)
    z.append(z[-1])
    v_z.append(v_z[-1])

plt.plot(x,y,'g-')
plt.title('y-x relation of a backspin baseball')
plt.xlabel('x dispalcement');plt.ylabel('y dispalcement')
plt.annotate('shoot range 243.3m(2000rpm)',xy=(243.3,0),xytext=(150,5),
arrowprops=dict(arrowstyle="->"))
print x[-1]
plt.savefig("y-x.png")
plt.show()