import os
import json
import glob
import re

###################################################################
###################################################################
###########PREFUCIO################################################
#-----------------------------------------------------------------#
#---DEBES CREAR UN "db.json" Y DENTRO ESCRIBIR: "{}"--------------#
#-----------------------------------------------------------------#
#---SE DEBE DE CREAR A MANO LA CARPETA "RandomSongs"--------------#
#-----------------------------------------------------------------#
###################################################################
###########COSAS PARTICULARES DE CADA ORDENADOR####################
#-----------------------------------------------------------------#
#---YO MUEVO TODO DENTRO DE LA CARPETA MÚSICA---------------------#
#---CADA PERSONA DEBE METERLO EN LA SUYA, COMO SE LLAME-----------#
#-----------------------------------------------------------------#
#---TAMBIEN PARA USAR GLOB (CLEAN MUSICA LIST) USO MI DIRECTORIO--#
#---SE DEBE CAMBIAR POR EL NOMBRE DE CADA UNO---------------------#
#-----------------------------------------------------------------#
###################################################################
###################################################################
print ("Welcome to Youtufy!")
option = 1
while option!="0":
	print("Enter the option:\n\t1-->Enter a list\n \t2-->Update system\n")
	option = input("\t3-->See the database\n \t4-->Edit database\n \t5-->Clean music list\n \t6-->Just one song\n \t0-->Exit\n")
	if option=="1":
		list_name = input("Enter the name of the list: ")
		url = input("Enter the new url: ")
		os.system("cd && cd Música && mkdir "+list_name+"&& cd "+list_name+" && youtube-dl --ignore-errors --literal --extract-audio --audio-format mp3 "+url)
		a_dict = {list_name: url}
		with open('db.json') as f:
			data = json.load(f)
		data.update(a_dict)
		with open('db.json', 'w') as f:
			json.dump(data, f)

	elif option=="2":
		print("Starting to open the database")
		json_data = open('db.json')
		data = json.load(json_data)
		for key in data:
			os.system("cd && cd Música && cd "+key+" && youtube-dl --ignore-errors --literal --extract-audio --audio-format mp3 "+data[key])

	elif option=="3":
		print("Starting to open the database")
		json_data = open('db.json')
		data = json.load(json_data)
		for key in data:
			print(key+"-------------- \t------------------------"+data[key])

	elif option=="4":
		print("Starting to open the database")
		json_data = open('db.json')
		data = json.load(json_data)
		i=0
		keys=[]
		for key in data:
			i+=1
			print(i,". \t"+key)
			keys.append(key)
		selection= input("Select the number of the playlist you want to erase: ")
		if selection>"0":
			data.pop(keys[int(selection)-1])
			with open('db.json', 'w') as f:
				json.dump(data, f)
			print("List erased from the database")
			print("Do you want to erase the all the local list? (This will erase all the music list)")
			local=input("y/n --> ")
			if local=="y":
				os.system("cd && cd Música && rm -r "+keys[int(selection)-1])
				print("List erased")
	elif option=="5":
		print("This will erase all repeated music from all your playlists")
		yesno =input("Do you want to continue? (y/n) ")
		if yesno=="y":
			print("Starting to open the database")
			json_data = open('db.json')
			data = json.load(json_data)
			data2=data
			for key in data:
				files=os.listdir("/home/carlos/Música/"+key)
				for key2 in data2:
					if key!=key2:
						files2=os.listdir("/home/carlos/Música/"+key2)
						for file1 in files:
							for file2 in files2:
								if file1==file2:
									print("Son igualicos illo")
									os.system("cd && cd Música/"+key+" && rm -r "+re.escape(file1))

	elif option==6:
		print("This song will be added to 'RandomSongs' directory")
		url = input("Enter the new url: ")
		os.system("cd && cd Música && cd RandomSongs && youtube-dl --ignore-errors --literal --extract-audio --audio-format mp3 "+url)


