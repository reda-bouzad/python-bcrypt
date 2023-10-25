import bcrypt

password = "mypassword"

bytes = password.encode('utf-8')

salt = bcrypt.gensalt()

hashedPassword = bcrypt.hashpw(bytes, salt)

print(hashedPassword)