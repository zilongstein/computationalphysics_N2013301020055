import numpy as np

class Potential:
    def __init__(self,_i=0,_j=0,_l=0,_m=0):
        self.b=np.zeros((11,11,100,100))
        self.i,self.j,self.l,self.m=_i,_j,_l,_m
        self.dV=1.0
        self.one=np.ones((9,1))
        self.dd=np.zeros((1,9))
        self.dd1=np.zeros((1,9))
        self.ss=0
    def b0(self):
        self.b[0,:11:1,:,:]=1
        self.b[10,:11:1,:,:]=-1
        while self.dV>0.001:
            while self.j<9:
                self.dd[0,self.j]=self.b[self.j+1,0,self.l,0]
                self.b[self.j+1,0,self.l+1,:]=(self.b[self.j,0,self.l,0]+self.b[self.j+2,0,self.l,0])/2
                self.b[self.j+1,10,self.l+1,:]=(self.b[self.j,10,self.l,0]+self.b[self.j+2,10,self.l,0])/2
                self.ss=self.b[self.j+1,0,self.l+1,0]-self.dd[0,self.j]
                self.dd[0,self.j]=abs(self.ss)
                print self.b[self.j+1,0,self.l,0],self.b[self.j+1,10,self.l,0],self.ss,self.dd[0,self.j]
                self.j+=1
            self.dV=np.dot(self.dd,self.one)
            self.l+=1
            self.j=0
            print self.dV
        print self.i,self.j,self.l
        self.dV=1
        self.l-=1
    def computation(self):
        while self.dV>0.001:
            while self.i<9:
                while self.j<9:
                    self.dd1[0,self.i]=self.b[self.i+1,5,self.l,self.m]
                    self.b[self.i+1,self.j+1,self.l,self.m+1]=(self.b[self.i,self.j+1,self.l,self.m]+self.b[self.i+2,self.j+1,self.l,self.m]+self.b[self.i+1,self.j,self.l,self.m]+self.b[self.i+1,self.j+2,self.l,self.m])/4
                    self.dd1[0,self.i]=abs(self.b[self.i+1,5,self.l,self.m+1]-self.dd1[0,self.i])
                    self.j+=1
                self.i+=1
                self.j=0
            self.m+=1
            self.i=0
            self.dV=np.dot(self.dd1,self.one)
        print self.b[:,:,self.l,self.m-1],self.m

p=Potential()
p.b0()
p.computation()