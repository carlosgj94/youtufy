import pymongo


print("This will help you configuring the system")
con = pymongo.Connection()
db = con.Youtufy
youtufy = db.configuration

conf= youtufy.find({"configuration":"yes"})
configuration=False
for key in conf:
	configuration=key["configuration"]
	music_name=key["music_name"]
	music_quality=key["music_quality"]
	username=key["username"]
if configuration=="yes":
	option=1
	while option != "0":
		print("Choose a option: ")
		option = input("\t1-->See the actual options\n \t2-->Default quality for downloads?\n \t3-->Music Directory:\n \t4-->Usename of the computer (usually is your name) \n \t0-->Exit\n")

		if option=="1":
			print("Max quality of downloads: "+music_quality)
			print("Music directory: "+music_name)
			print("Username: "+username)
			
		elif option=="2":
			music_quality = input("Do you want the max quality?\n This will make longer the downloads and heavier the files, sorry\n ( yes/no ) --> ")
			youtufy.update({"configuration":"yes"}, {"configuration":"yes", "music_name":music_name, "music_quality":music_quality, "username":username})

		elif option=="3":
			music_name= input("Enter the name of your music directory: ")
			youtufy.update({"configuration":"yes"}, {"configuration":"yes", "music_name":music_name, "music_quality":music_quality, "username":username})

		elif option=="4":
			username = input("Enter the username: ")
			youtufy.update({"configuration":"yes"}, {"configuration":"yes", "music_name":music_name, "music_quality":music_quality, "username":username})

else:
	music_name= input("Enter the name of your music directory: ")
	music_quality = input("Do you want the max quality?\n This will make longer the downloads and heavier the files, sorry\n ( yes/no ) --> ")
	if music_quality != "yes" and music_quality!="no":
		music_quality = input("Choose a valid option: ")
	username = input("Enter the username: ")
	configuration_dict={"configuration":"yes", "music_name":music_name, "music_quality":music_quality, "username":username}
	youtufy.insert(configuration_dict) 