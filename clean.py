import os

arr = []
filename = "clean.py"

for file in os.listdir(os.getcwd()):
	if(os.path.isfile(file)):
		if(file !=  filename):
			name,ext = os.path.splitext(file)
			arr.append(ext)

# print(arr)

res = []
for	ext in arr:
	if ext not in res:
		res.append(ext)

flag = 0
for file in os.listdir(os.getcwd()):
	if(file == "RestoredFiles"):
		flag = 1
		
if(flag != 1):
	os.mkdir("RestoredFiles")

currentDir = os.getcwd()

#Restored Directory
resDir = currentDir + "/RestoredFiles"
os.chdir(resDir)

for ext in res:
	name = ext.replace(".","")
	d = "./" + name
	if(os.path.isdir(d) != True):
		os.mkdir(name)

os.chdir(currentDir)

#print(os.getcwd())

for file in os.listdir(os.getcwd()):
 	if(os.path.isfile(file)):
 		if(file != filename):
	 		name,ext = os.path.splitext(file)
	 		newName = ext.replace(".","");
	 		source = currentDir + "/" + file
	 		dest = currentDir + "/RestoredFiles/" + newName + "/" + file
	 		os.rename(source,dest)
	
