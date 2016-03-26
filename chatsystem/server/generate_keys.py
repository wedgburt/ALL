from Crypto.PublicKey import RSA
"""
Generates a new public/private key pair 
"""
new_key = RSA.generate(2048)
public_key = new_key.publickey().exportKey("PEM") 
private_key = new_key.exportKey("PEM")

f = open('priv.pem','w')
f.write(private_key)
f.close()

f = open('../client/pub.pem','w')
f.write(public_key)
f.close()
