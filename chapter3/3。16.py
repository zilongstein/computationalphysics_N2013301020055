from math import *
from pylab import *



fd=0

while fd =[1.5]:
    theta=[0.2]
    omega=[2]
    time=[0]
    dt,i,n=0.1,0,0


    while time[i]<=5000:    
        omega.append(omega[i]+(-sin(theta[i])-0.5*omega[i]+fd*sin(time[i]*2/3))*dt)
        char=theta[i]+omega[i+1]*dt
        if theta[i]+omega[i+1]*dt<-pi:        
            theta.append(char+2*pi)
        elif theta[i]+omega[i+1]*dt>pi:
            theta.append(char-2*pi)
        else:
            theta.append(char)
        time.append(time[i]+dt)    
        i=i+1

    plt.figure(figsize=(18,9))
    subplot(1,2,1)
    plt.title("$\Theta$ versus $time$,FD="+str(fd)+",$\Theta$(0)=0.2,$\omega$(0)=0")
    plt.xlim(0,150)
    plt.plot(time,theta)
    plt.xlabel("$time(s)")
    plt.ylabel("$\Theta(radius)")
    subplot(1,2,2)
    plt.title("$\omega$ versus $\Theta$,FD="+str(fd)+",$\Theta$(0)=0.2,$\omega$(0)=0")
    plt.xlim(-4,4)
    plt.ylim(-3,1)
    plt.xlabel("$\Theta$(radians)")
    plt.ylabel("$\omega$(radians/s)")
    while 3*n*pi<=time[-1]:
        plt.scatter(theta[int(3*n*pi/dt)],omega[int(3*n*pi/dt)],color="yellow",linewidth=0.01)
        n=n+1
    plt.show()