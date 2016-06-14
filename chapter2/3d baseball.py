# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 21:44:53 2016

@author: john
"""

# -*- coding: utf-8 -*-
from visual import *
from math import *
ball=sphere(pos=(-158,0,1.8),radius=1,color=color.white,material=materials.rough)
ball.velocity=vector(45,0,30)

wallL=box(pos=(-160,0,60),size=(2,120,120),color=color.blue,material=materials.rough)
ground=box(pos=(0,0,0),size=(320,120,0.2),color=color.orange,material=materials.marble)
wallB=box(pos=(0,60,60),size=(320,0.2,120),color=color.red,material=materials.diffuse)

ball.trail=curve(color=ball.color)

vscale=0.2
varr=arrow(pos=ball.pos,axis=vscale*ball.velocity,color=color.yellow)

deltat=0.005
g=-9.8;Sm=2*10**(-4);w=209.44;Bm=-0*10**(-3)

text=label (text="pitcher",pos=(-160,0,0), xoffset=20,yoffset=50,border=4)
text=label (text="home plate",pos=(160,0,0), xoffset=20,yoffset=-50,border=4)
text=label (text="playground",pos=(0,-60,0), xoffset=20,yoffset=-50,border=4)
text=label (text="wall",pos=(0,60,100), xoffset=20,yoffset=50,border=4)


while ball.pos.z-ball.radius>=0:
    rate(1000)
    if ball.pos.y+ball.radius>wallB.y:
        ball.velocity.y=-ball.velocity.y
    ball.pos=ball.pos+ball.velocity*deltat
    ball.v=math.sqrt(ball.velocity.x**2+ball.velocity.y**2+ball.velocity.z**2)
    ball.velocity.x=ball.velocity.x+deltat*Bm*ball.v*ball.velocity.x
    ball.velocity.y=ball.velocity.y+deltat*Sm*w*ball.velocity.x+deltat*Bm*ball.v*ball.velocity.y
    ball.velocity.z=ball.velocity.z+deltat*g+deltat*Bm*ball.v*ball.velocity.z
    
    varr.pos=ball.pos
    varr.axis=vscale*ball.velocity
    
    ball.trail.append(pos=ball.pos)

print '棒球的射程:',ball.pos.x+158