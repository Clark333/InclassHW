close all
clear all
clc

syms x1 x2 t 
A = [0,1;-1,0]
[P,D] = eig(A)

y0 = [1;0]

v0 = P^-1*y0

v = expm(t*D)*v0

display(' ')
display('******** Y ******')
display(' ')
pretty(P*v)
simplify(P*v)
