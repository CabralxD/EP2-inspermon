#inspermons:
pythonxu={"ataque":30,"defesa":20,"vida":100} #N:0
fegamel={"ataque":40,"defesa":50,"vida":70} #N:1
deusvult={"ataque":50,"defesa":10,"vida":50} #N:2

insperdex=[["pythonxu",50,20,100,"N:0"],["fegamel",40,40,70,"N:1"],["deusvult",55,10,50,"N:2"]]
insperdéx=["-"]*20
XP=0

import time
import random

def batalha(mon,ini,insperdéx,insperdex):
	print("seu inspermon: {},ataque:{},defesa{},vida:{}".format(insperdex[mon][0],insperdex[mon][1],insperdex[mon][2],insperdex[mon][3]))
	print("""inspermon selvagem: {},
		               ataque: {},
		               defesa: {},
		               vida: {}""".format(insperdex[ini][0],insperdex[ini][1],insperdex[ini][2],insperdex[ini][3]))
	
	vidaini=insperdex[ini][3]
	vidajog=insperdex[mon][3]
	
	while vidajog>0 and vidaini>0:
	 	print("você atacou!")
	 	w=random.randint(0,19)
	 	if w==10:
	 		print("ataque crítico!")
	 		if ((insperdex[mon][1]*1.5)-(insperdex[ini][2]))<0:
	 			print("o inspermon inimigo se defendeu do ataque!")
	 		else:
	 			vidaini=(vidaini)-((insperdex[mon][1]*1.5)-(insperdex[ini][2]))
	 	if w!=10:
	 		if ((insperdex[mon][1])-(insperdex[ini][2]))<0:
				print ("O inspermon inimigo se defendeu do ataque!")
			else:
				vidaini=(vidaini)-((insperdex[mon][1])-(insperdex[ini][2]))

	 	
	 	print("a vida do seu inimigo agora é de: {}".format(vidaini))
	 	
	 	if vidaini>0:
	 		print ("seu oponente ataca!")
	 		if (insperdex[ini][1]-insperdéx[mon][2])<0:
	 			print("O seu inspermon se defendeu do ataque inimigo!")
	 		else:	
	 			vidajog=vidajog-(insperdex[ini][1]-insperdéx[mon][2])
	 		print("a vida de seu inspermon agora é de: {}".format(vidajog))
	 		q=input("oque você quer fazer: 'lutar' ou 'fugir'?")
	 	if q=="fugir":
	 		break
	 
	if vidaini<=0:
		print ("você venceu!")
		if not(insperdex[ini] in insperdéx):
			insperdéx[ini]=(insperdex[ini])
			command="nada"

	if vidajog<=0:
		print("você perdeu...")
		command="dormir"

	if q=="fugir":
		print("você fugiu")
		command="nada"
	
	return (command)

	 
	

		

print ("Olá!")
time.sleep(2)
print("Bem vindo à inspermon!")
time.sleep(2)
print ("Vamos começar!")
time.sleep(2)
print("você vai precisar de um insperdéx...")
time.sleep(2)
print("agora é hora de escolher o seu primeiro inspermon para começar a sua aventura!")
time.sleep(4)
insp=input("escolha um inspermon: pythonxu, fegamel, deusvult: ")

if insp=="pythonxu":
	insperdéx[0]=(insperdex[0])
	mon=0
	
if insp=="fegamel":
	insperdéx[1]=(insperdex[1])
	mon=1
if insp=="deusvult":
	insperdéx[2]=(insperdex[2])
	mon=2

time.sleep(1.5)
print("você escolheu {}!".format(insperdex[mon][0]))
command="nada"

time.sleep(2.5)
print("lembresse: quando você vir a opção 'o que você quer fazer?' você pode escolher:")
print("------passear (para achar inspermons)")
print("------dormir (para retornar a sua casa e sair do jogo)")
print("------insperdéx (para ver os innspermons que você encontrou e venceu)")
print("------trocar (para substituir o inspermon que você utilizara na próxima batalha)")


while command!="dormir":
	command=input("oque voce quer fazer?: ")
	for h in range (3):
		print("...")
		time.sleep(1)

	if command=="passear":
		ini=random.randint(0,2)
		command=batalha(mon,ini,insperdéx,insperdex)
		if command!="dormir"
			XP=XP+1
			print("seu inspermon ganhou experiência!")
		
		if XP==10:
			for h in range (3):
				print("...")
				time.sleep(1)
			for i in range(1,3):
				insperdéx[mon][i]=insperdéx[mon][i]+5
				print("seu inspermon evoluiu!")
				print(insperdéx[mon])
				XP=1


	if command=="insperdéx":
		for h in range(len(insperdéx)):
			print(insperdéx[h])
	
	if command=="trocar":
		for h in range(len(insperdéx)):
			print(insperdéx[h])
		print("escolha um inspermon de seu insperdéx")
		y=mon
		x=input("diga o número do inspermon você gostaria de utilizar?: ")
		mon=x
		if not (x in insperdéx):
			mon=y 

	else:
		for h in range(3):
			print(".",end="")
			time.sleep(1)











print("você está em  casa!\n até a próxima!\n")