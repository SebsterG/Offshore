import numpy as np 
import matplotlib.pyplot as plt
pressure_array = np.zeros(30)
eps = 5*10**-5
ny = 2 *10**-5
d1 = 0.127
d2 = 0.305
h1 = -4000
h2 = -1000
l1 = -h1
l2 = 50000
def pressure_calculator_1(P,D,u,h,l):
	return hydrostatic(P,h) + friction(D,P,u,l)
def friction(D,P,u,l):
	return (-1.8*np.log10((eps/(D*3.7))**1.11 + 6.9/Re(P,u,D)))**-2 *( l*0.5*rho(P)*u**2)/D
def hydrostatic(P,h):
	return -rho(P)*9.81*h 
def rho(P):
	return 0.73*P + 0.123
def Re(P,u,D):
	return rho(P)*u * D/ny
"""def Temp(T_sea,T0,D,U,m,Cp,x):
	return T_sea + (T0-T_sea)*np.exp(-np.pi*D*U*x/(m*Cp))
T_sea = 7 +273
T0 = 150 + 273
U1 = 1
U2 = 1
Cp = 2000
m = [30,25,20,17,14]
x2 = np.linspace(0,50000,50001)
x1 = np.linspace(0,4000,4001)
Pressure_arr = [360,300,240,180,120]
for i in m:
	temp = Temp(T_sea=(T_sea+T0)/2,T0=T0,D=d1,U=U1,m=i,Cp=Cp,x=x1)
	fig = plt.figure(1)
	ax = fig.add_subplot(111)
	#ax.plot(x1,temp-273)
	temp2 = Temp(T_sea=T_sea,T0=temp[-1],D=d2,U=U2,m=(i*2),Cp=Cp,x=x2)
	ax.plot(x2,temp2-273)
	print temp-273

ax.legend(["Q=%d " %(2*b) for b in m ])
plt.show()
"""
def constant(x):
	return 50
const = np.linspace(1,30,31)
const[:] = 50
P_start = 360 + 50
i = 0
p2 = P_start
while p2 > 20:
	i += 1
	del_p1 = pressure_calculator_1(P=P_start,D=d1,u=2,h=h1,l=l1)/10**6
	p1 = P_start - del_p1
	pressure_array[i-1] = p1
	del_p2 = pressure_calculator_1(P=p1,D=d2,u=2,h=h2,l=l2)/10**6
	p2 = p1 - del_p2
	pressure_array[i] = p2
	
	P_start = P_start - 15
	
	print "Year: ",i, "---", "Pressure topside: ", p2
#print i
#print pressure_array


plt.plot(pressure_array)
plt.plot(const,'r')
plt.title(" Pressure onshore vs time")
plt.xlabel("Time[years]")
plt.ylabel("Pressure[bar]")
plt.show()




