from Crypto.Cipher import AES
from Crypto import Random
  
key = Random.new().read(AES.block_size)  
iv = Random.new().read(AES.block_size) 

print("iv="+iv.hex()) 
print("key="+key.hex())  

BS = 16  
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 

f=open('plaintext.txt')
msg=f.read() 
print("plaintext:"+msg)

# Encryption
cbc_cipher = AES.new(key, AES.MODE_CBC, IV=iv)
cipher_text = iv + cbc_cipher.encrypt(pad(msg).encode())  
print ('CBC Mode Encrypted Text: ', cipher_text.hex().upper() )