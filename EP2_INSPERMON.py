#inspermons:
pythonxu={"ataque":30,"defesa":20,"vida":100}
fegamel={"ataque":40,"defesa":50,"vida":70}
deusvult={"ataque":50,"defesa":10,"vida":50}

insperdex=[["pythonxu",30,20,100],["fegamel",40,50,70],["deusvult",50,10,50]]
insperdéx=[]

import time
import random

def batalha(mon,ini,insperdéx,insperdex):
	print("seu inspermon: {},ataque:{},defesa{},vida:{}".format(insperdex[mon][0],insperdex[mon][1],insperdex[mon][2],insperdex[mon][3])
	print("inspermon selvagem: {},ataque:{},defesa{},vida:{}".format(insperdex[ini][0],insperdex[ini][1],insperdex[ini][2],insperdex[ini][3])
	vidaini=insperdex[ini][3]
	vidajog=insperdex[mon][3]
	while vidajog>0 and vidaini>0:
	 	print("você atacou!")
	 	vidaini=(vidaini)-(insperdex[mon][1])-(insperdex[ini][2])
	 	print("a vida do seu inimigo agora é de: {}".format(vidaini))
	 	if vidaini>0:
	 		print ("seu oponente ataca!")
	 		vidajog=vidajog-(ataquedoini)-(defdojog)
	 		print("a vida de seu inspermon agora é de: {}".format(vidajog))
	 
	if vidaini<=0:
		print ("você venceu!")
		if not(insperdex[ini] in insperdéx):
		insperdéx.append(insperdex[ini])


	if vidajog<=0:
		print("você perdeu...")
		t="dormir"


		



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
	insperdéx.append(insperdex[0])
	mon=0
	
if insp=="fegamel":
	insperdéx.append(insperdex[1])
	mon=1
if insp=="deusvult":
	insperdéx.append(insperdex[2])
	mon=2

t="nada"
print("lembresse: quando você vir a opção 'o que você quer fazer?' você pode escolher:")
print("------passear (para achar inspermons)")
print("------dormir (para retornar a sua casa e sair do jogo)")
print("------insperdéx (para ver os innspermons que você encontrou e venceu)")


while t!="dormir":
	t=input("oque voce quer fazer?")
	for h in range (3):
		print("...")
		time.sleep(1)

	if t=="passear":
		ini=random.randint(0,2)
		batalha(mon,ini,insperdéx,insperdex)

	if t=="insperdéx":
		print(insperdéx)









print("você está em  casa!\n até a próxima!\n")