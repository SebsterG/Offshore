import matplotlib.pyplot as plt
import numpy as np
T = 10.0
dt = 0.01
Nt = int(round(T / float(dt)))

g = 9.81   #m/s^2
m = 50000.0 #Kg
rho = 1000.0 #Kg/m^2
C_D = 0.2 
S = 1.5 #m^2

u = np.zeros(Nt+1)
N = 0
u[0] = 0
for n in range(Nt):
	u[n+1] = u[n] + dt*(g - (1./(2.0*m)) * rho * C_D * S * (u[n])**2 )
	if u[n] > 50.1:
		N = n
		break
t = np.linspace(0,T,Nt)		
u_traps = u[1:N]

fig = plt.figure()
plt.plot(t[0:N+2],u[:N+2], "r")
fig.suptitle('Velocity vs time of falling anchor', fontsize=14, fontweight='bold')

ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)

ax.set_xlabel('Time s')
ax.set_ylabel('Velocity m/s')

ax.text(0.7, 3,"It takes %.2f seconds and %.2f m to reach a  velocity of 50 m/s" %(t[N],np.trapz(u_traps, x=None, dx=dt ))
, style='italic',
        bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})

plt.show()


