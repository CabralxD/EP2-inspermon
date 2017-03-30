L=20
Lc=25
Ac=1000
A=1500
gama=0.056
beta=0.025
t=0
listaL=[0]*500
listaA=[0]*500
listaL[0]=L
listaA[0]=A
while t<500-1:
    deltaL=(((gama*L*A)/Ac)-(gama*L))
    listaL[t+1]=listaL[t]+deltaL
    deltaA=((beta*A)-((beta*L*A)/Lc))
    listaA[t+1]=listaA[t]+deltaA
    t=t+1
print (listaL)
print (listaA)