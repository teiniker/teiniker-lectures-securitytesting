# information from static reverse engineering
hardcoded_password = 'xywjslljmjnr'
key = 5

# Decrypt the hardcoded password
password_bytes = bytearray(hardcoded_password, 'utf-8')
for i in range (len(password_bytes)):
    password_bytes[i] = password_bytes[i] - key    
password = password_bytes.decode("utf-8") 
print(password)