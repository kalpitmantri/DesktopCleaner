import os

arr = []

for file in os.listdir(os.getcwd()):
	if(os.path.isfile(file)):
		name,ext = os.path.splitext(file)
		arr.append(ext)

# print(arr)

res = []
for	ext in arr:
	if ext not in res:
		res.append(ext)

os.mkdir("RestoredFiles")

currentDir = os.getcwd()

#Restored Directory
resDir = currentDir + "/RestoredFiles"
os.chdir(resDir)

for ext in res:
	name = ext.replace(".","")
	os.mkdir(name)

os.chdir(currentDir)

# print(os.getcwd())

for file in os.listdir(os.getcwd()):
 	if(os.path.isfile(file)):
 		name,ext = os.path.splitext(file)
 		newName = ext.replace(".","");
 		source = currentDir + "/" + file
 		dest = currentDir + "/RestoredFiles/" + newName + "/" + file
 		os.rename(source,dest)
