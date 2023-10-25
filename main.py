import bcrypt

# example password 
password = "mypassword"

# converting password to array of bytes 
bytes = password.encode('utf-8')

# generating the salt 
salt = bcrypt.gensalt()

# Hashing the password 
hashedPassword = bcrypt.hashpw(bytes, salt)

# Taking user entered password  
userPassword =  'password000'

# encoding user password 
userBytes = userPassword.encode('utf-8') 
  
# checking password 
result = bcrypt.checkpw(userBytes, hashedPassword) 


print(hashedPassword)
print(result)