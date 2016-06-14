import math
import matplotlib.pyplot as plt

x=[];y=[];v_x=[];v_y=[];t=[];i=[];theta_list=[];x_list=[]
dt=0.01;g=-9.8;v_init=800*2**0.5

for theta in range(30,61):
    i.append(0)
    v_x.append(v_init*math.cos(theta*math.pi/180))
    v_y.append(v_init*math.sin(theta*math.pi/180))
    x.append(0.0)
    y.append(0.0)
    t.append(0.0)
    while y[-1]>=0.0:
        x_tmp=x[-1]+dt*v_x[-1]
        x.append(x_tmp)
        v_x_tmp=v_x[-1]
        v_x.append(v_x_tmp)
        y_tmp=y[-1]+dt*v_y[-1]
        y.append(y_tmp)
        v_y_tmp=v_y[-1]+dt*g
        v_y.append(v_y_tmp)
        i_tmp=i[-1]+1
        i.append(i_tmp)
        t.append(dt*i[-1])        
     
    theta_list.append(theta);x_list.append(x[-1])
    
plt.plot(theta_list,x_list,'og' , label="(theta,shoot range)")
plt.xlabel("theta/$\circ$")
plt.ylabel("shoot range/m")
plt.title('the relationship bewteen theta and shoot range of a cannon shell')
plt.legend()
plt.savefig('no drag cannon.png')
plt.show()