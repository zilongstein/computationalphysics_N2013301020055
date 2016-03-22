#第一章习题1.3报告
##摘要
####  利用题中所给的微分方程编程描述了考虑空气阻力情况下一个小球从高处落下，其速度随时间变化的关系。
####$$v(\Delta t)=V(0)+\frac{dv(t)}{dt}\Delta t+\frac{1}{2} \frac{d^2v(t)} {d^2t}(\Delta t)^2+······$$ 只保留一阶项有： $$V(\Delta t)≈V(0)+\frac{dv}{dt}\Delta t$$整理的： $$\frac{dv(t)}{dt}=\lim_{\Delta t\to 0} \frac{v(t+\Delta t)-v(t)}{\Delta t}≈ \frac{v(t+\Delta t)-v(t)}{\Delta t}$$ 因为：$\frac{dv}{dt}=a-bv$，带入上式得： $$v(t+\Delta t)≈v(t)+(a-bv)\Delta t$$
