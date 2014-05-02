import os
import re
import pymongo
###################################################################
###################################################################
###########PREFUCIO################################################
#-----------------------------------------------------------------#
#---SE DEBE DE CREAR A MANO LA CARPETA "RandomSongs"--------------#
#-----------------------------------------------------------------#
###################################################################
###########COSAS PARTICULARES DE CADA ORDENADOR####################
#-----------------------------------------------------------------#
#---YO MUEVO TODO DENTRO DE LA CARPETA MÚSICA---------------------#
#---CADA PERSONA DEBE METERLO EN LA SUYA, COMO SE LLAME-----------#
#-----------------------------------------------------------------#
#---TAMBIEN PARA USAR re (CLEAN MUSICA LIST) USO MI DIRECTORIO--#
#---SE DEBE CAMBIAR POR EL NOMBRE DE CADA UNO---------------------#
#-----------------------------------------------------------------#
###################################################################
###################################################################
#HAY QUE CAMBIAR TMP POR Música!!!!!

print ("Welcome to Youtufy!")
option = 1
con = pymongo.Connection()
db = con.Youtufy
youtufy = db.playlist
while option!="0":
	print("Enter the option:\n\t1-->Enter a list\n \t2-->Update system")
	option = input("\t3-->See the database\n \t4-->Edit database\n \t5-->Clean music list\n \t6-->Just one song\n \t0-->Exit\n")
	if option=="1":
		list_name = input("Enter the name of the list: ")
		url = input("Enter the new url: ")
		update = input("Do you want to keep update the playlist? (y/n): ")
		a_dict = {"name":list_name, "url": url, "update":update}
		youtufy.insert(a_dict)
		os.system("cd && cd Música && mkdir "+list_name+"&& cd "+list_name+" && youtube-dl --ignore-errors -o '%(title)s.%(ext)s'  --extract-audio --audio-format mp3 --audio-quality 0 "+url)		

	elif option=="2":
		print("Starting to open the database")
		y_update = youtufy.find({'update':'y'})
		multiple = input("Do you want to get update one or more playlist? \n \t 1--> All \n \t 2-->One \n")
		if multiple =="1":
			for key in y_update:
				os.system("cd && cd Música && cd "+key['name']+" && youtube-dl --ignore-errors -o '%(title)s.%(ext)s'  --extract-audio --audio-format mp3 --audio-quality 0 "+key['url'])
		elif multiple=="2":
			y_all = youtufy.find()
			i=0
			urls=[]
			names=[]
			for key in y_all:
				i+=1
				print(i,". \t"+key["name"])
				urls.append(key["url"])
				names.append(key["name"])
			selection= input("Select the number of the playlist you want to update: ")
			if selection>0:
				os.system("cd && cd Música && cd "+names[int(selection)-1]+" && youtube-dl --ignore-errors -o '%(title)s.%(ext)s'  --extract-audio --audio-format mp3 --audio-quality 0 "+urls[int(selection)-1])
		else:
			print("You didn't choose a valid option")

	elif option=="3":
		print("Starting to open the database")
		y_all = youtufy.find()
		for key in y_all:
			print(key["name"]+"\t"+key["url"]+"\tKeep Update: "+key["update"])

	elif option=="4":
		print("Starting to open the database")
		y_all = youtufy.find()
		i=0
		keys=[]
		for key in y_all:
			i+=1
			print(i,". \t"+key["name"])
			keys.append(key["name"])
		selection= input("Select the number of the playlist you want to erase: ")
		if selection>"0":
			youtufy.remove({"name":keys[int(selection)-1]})
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
			y_all = youtufy.find()
			y_all2= y_all
			for key in y_all:
				files=os.listdir("/home/carlos/Música/"+key["name"])
				for key2 in y_all2:
					if key["name"]!=key2["name"]:
						files2=os.listdir("/home/carlos/Música/"+key2["name"])
						for file1 in files:
							for file2 in files2:
								if file1==file2:
									print("Son igualicos illo")
									os.system("cd && cd Música/"+key["name"]+" && rm -r "+re.escape(file1))

	elif option=="6":
		print("This song will be added to 'RandomSongs' directory")
		url = input("Enter the new url: ")
		os.system("cd && cd Música && cd RandomSongs && youtube-dl --ignore-errors -o '%(title)s.%(ext)s'  --extract-audio --audio-format mp3 --audio-quality 0 "+url)


