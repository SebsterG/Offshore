import numpy as np 
eps = 5*10**-5
ny = 2 *10**-5
d1 = 0.127
d2 = 0.30
h1 = -4000
h2 = -1000
l1 = -h1
l2 = 50000
def pressure_calculator_1(P,D,u,h,l):
	return hydrostatic(P,h) + 2*friction(D,P,u,l)
def pressure_calculator_2(P,D,u,h,l):
	return hydrostatic(P,h) + friction(D,P,u,l)
def friction(D,P,u,l):
	return (-1.8*np.log10((eps/(D*3.7))**1.11 + 6.9/Re(P,u,D)))**-2 *( l*0.5*rho(P)*u**2)/D
def hydrostatic(P,h):
	return -rho(P)*9.81*h 
def rho(P):
	return 0.73*P + 0.123
def Re(P,u,D):
	return rho(P)*u * D/ny

del_p1 = pressure_calculator_1(P=360,D=d1,u=2,h=h1,l=l1)/10**6
p1 = 360 -del_p1
del_p2 = pressure_calculator_2(P=p1,D=d2,u=2,h=h2,l=l2)/10**6
p2 = p1 - del_p2
print del_p1
print p1
print del_p2
print p2

