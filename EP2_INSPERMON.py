pythonxu={"ataque":30,"defesa":20,"vida":100} #N:0   
fegamel={"ataque":40,"defesa":40,"vida":70} #N:1
deusvult={"ataque":50,"defesa":20,"vida":80} #N:2         # Os 5 primeiros são pokemons de valores "mais fracos"
bubbassalto={"ataque":55,"defesa":20,"vida":75} #N:3
charmandela={"ataque":35,"defesa":45,"vida":70} #N:4
feche={"ataque":40,"defesa":30,"vida":110} #N:5
celera={"ataque":50,"defesa":50,"vida":80} #N:6
alohomora={"ataque":60,"defesa":30,"vida":90} #N:7        # 5 pokemons intermediários
cartertorta={"ataque":65,"defesa":30,"vida":85} #N:8
zubate={"ataque":45,"defesa":55,"vida":80} #N:9
roberstoise={"ataque":50,"defesa":40,"vida":120} #N:10
karcana={"ataque":60,"defesa":60,"vida":90} #N:11
nihibloco={"ataque":70,"defesa":40,"vida":100} #N:12      # Os mais fortes
viguvigu={"ataque":75,"defesa":40,"vida":95} #N:13
fairinhow={"ataque":55,"defesa":65,"vida":90} #N:14


insperdex=[["pythonxu",50,20,100,"N:0"],["fegamel",40,40,70,"N:1"],["deusvult",55,10,50,"N:2"],["bubbassalto",55,20,80,"N:3"],["charmandela",35,45,70,"N:4"],
["feche",40,30,110,"N:5"],["celera",50,50,80,"N:6"],["alohomora",60,30,90,"N:7"],["cartertorta",65,30,90,"N:8"],["zubate",45,55,80,"N:9"],["robertoise",50,40,120,"N:10"],
["karcana",60,60,90,"N:11"],["nihibloco",70,40,100,"N:12"],["viguvigu",75,40,95,"N:13"],["fairinhow",55,65,90,"N:14"]]
insperdéx=["-"]*20
XP=0
LV=0

import time
import random

command="NADA"

def batalha(mon,ini,insperdéx,insperdex):
    print("Um Inspermón selvagem apareceu!")
    time.sleep(1.5)
    print("Seu Inspermon: {},ataque:{},defesa:{},vida:{}".format(insperdex[mon][0],insperdex[mon][1],insperdex[mon][2],insperdex[mon][3]))
    time.sleep(1)
    print("""inspermon selvagem: {},
		               ataque: {},
		               defesa: {},
		               vida: {}""".format(insperdex[ini][0],insperdex[ini][1],insperdex[ini][2],insperdex[ini][3]))
	
    vidaini=insperdex[ini][3]
    vidajog=insperdex[mon][3]
	
    while vidajog>0 and vidaini>0:
        
        if vidajog>0 and vidaini>0:
            q= str(input("O que você quer fazer: 'lutar' ou 'fugir'?")).upper()
        
        if q=="LUTAR":
            print("Você atacou!")
            w=random.randint(0,19)
        
            if w==10:       #ataque crítico!
                print("Ataque C R Í T I C O!!!")
            
                if ((insperdex[mon][1]*1.5)-(insperdex[ini][2]))<0:
                    print("O Inspermon inimigo conseguiu se defender!")
            
                else:
                    vidaini=(vidaini)-((insperdex[mon][1]*1.5)-(insperdex[ini][2]))
                    print("A vida do seu inimigo agora é de {}".format(vidaini))

            else:    #ataque normal
                
                if ((insperdex[mon][1])-(insperdex[ini][2]))<0:
                	print ("O inspermon inimigo se defendeu do ataque!")
                
                else:
                	vidaini=vidaini-((insperdex[mon][1])-(insperdex[ini][2]))
                	print("A vida do seu inimigo agora é de: {}".format(vidaini))
		
        	
            
            if vidaini>0:
            	
                print ("Seu oponente ataca!")
                time.sleep(1)
                if (insperdex[ini][1]-insperdéx[mon][2])<=0:
                	print("O seu Inspermon se defendeu do ataque inimigo!")
                else:	
                	vidajog=vidajog-(insperdex[ini][1]-insperdéx[mon][2])
                	print("A vida de seu Inspermon agora é de: {}".format(vidajog))
               
	 
            if vidaini<=0:
            	print ("Você venceu!!!")
            	if not(insperdex[ini] in insperdéx):
                	insperdéx[ini]=(insperdex[ini])
                	print("Parabéns!!! Você capturou um novo Inspermon!!!")
            	command="NADA"
        	
            if vidajog<=0:
            	print("Você perdeu...")
            	command="DORMIR"

        
        
        if q=="FUGIR":
            print("Você fugiu!")
            command="FUGA"
            break
    
	
    return (command)


	 
	

for h in range(20):
	print(" ")		




print ("Olá!")
time.sleep(2)
print("Bem vindo à Inspermon!")
time.sleep(2)
print ("Vamos começar!")
time.sleep(2)
print("Você vai precisar de um Insperdéx...")
time.sleep(2)
print("Agora, é hora de escolher o seu primeiro Inspermon para começar a sua aventura!")
time.sleep(4)
insp= str(input("Escolha um Inspermon: pythonxu, fegamel, deusvult: ")).upper()

if insp=="PYTHONXU":
	insperdéx[0]=(insperdex[0])
	mon=0
	
if insp=="FEGAMEL":
	insperdéx[1]=(insperdex[1])
	mon=1

if insp=="DEUSVULT":
	insperdéx[2]=(insperdex[2])
	mon=2

time.sleep(1.5)
print("Você escolheu {}!".format(insperdex[mon][0]))
command="nada"

time.sleep(2.5)
print("Lembre-se: quando você vir a opção 'O que você quer fazer?', Você poderá escolher entre:")
print("------passear (para achar inspermons)")
print("------dormir (para retornar a sua casa e sair do jogo)")
print("------insperdéx (para ver os innspermons que você encontrou e venceu)")
print("------trocar (para substituir o inspermon que você utilizara na próxima batalha)")


while command!="DORMIR":
	command=str(input("O que voce quer fazer?: ")).upper()
	
	for h in range (3):
		print("...")
		time.sleep(1)

	if command=="PASSEAR":
		ini=random.randint(0,14)
		command=batalha(mon,ini,insperdéx,insperdex)
		if command=="NADA":
			XP=XP+1
			print("Seu Inspermon ganhou experiência!")
		
		if XP==10:
			for h in range (3):
				print("...")
				time.sleep(1)
			for i in range(1,3):
				insperdéx[mon][i]=insperdéx[mon][i]+5
			print("Seu Inspermon evoluiu!")
			print(insperdéx[mon])
			XP=1
			LV=LV+1


	if command=="INSPERDÉX":
		for h in range(len(insperdéx)):
			print(insperdéx[h])
	
	if command=="TROCAR":
		for h in range(len(insperdéx)):
			print(insperdéx[h])
		print("Escolha um Inspermon de seu Insperdéx")
		y=mon
		x=input("Diga o número do Inspermon você gostaria de utilizar: ")
		mon=x
		if not (x in insperdéx):
			mon=y 

	else:
		for h in range(3):
			print(".",end="")
			time.sleep(1)











print("Você está em  casa!\n Até a próxima!\n")